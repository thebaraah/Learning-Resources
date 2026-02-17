/**
 * Generates a short two-tone ascending chime WAV file (WhatsApp-style).
 *
 * Two quick sine tones: C5 (523Hz) → E5 (659Hz), each ~150ms,
 * with smooth attack/decay envelopes and a subtle harmonic overtone.
 *
 * Output: portal/public/notification.wav (~26KB, 16-bit PCM, 44100Hz, mono)
 *
 * Usage: node scripts/generate-notification.js
 */

import { writeFileSync } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUTPUT_PATH = resolve(__dirname, '../portal/public/notification.wav');

const SAMPLE_RATE = 44100;
const BITS_PER_SAMPLE = 16;
const NUM_CHANNELS = 1;

// Tone definitions
const tones = [
  { freq: 523.25, start: 0, duration: 0.1 }, // C5
  { freq: 659.25, start: 0.1, duration: 0.1 }, // E5
];

const OVERTONE_RATIO = 2; // 2nd harmonic
const OVERTONE_GAIN = 0.15; // subtle warmth
const MASTER_GAIN = 0.35;

const totalDuration = 0.3; // seconds
const numSamples = Math.ceil(SAMPLE_RATE * totalDuration);

// Generate samples
const samples = new Float64Array(numSamples);

for (const tone of tones) {
  const startSample = Math.floor(tone.start * SAMPLE_RATE);
  const toneSamples = Math.floor(tone.duration * SAMPLE_RATE);

  // Attack/decay envelope durations (in samples)
  const attackSamples = Math.floor(0.01 * SAMPLE_RATE); // 10ms attack
  const decaySamples = Math.floor(0.03 * SAMPLE_RATE); // 30ms decay

  for (let i = 0; i < toneSamples; i++) {
    const t = i / SAMPLE_RATE;

    // Envelope: smooth attack and decay to avoid clicks
    let envelope = 1.0;
    if (i < attackSamples) {
      envelope = i / attackSamples; // linear attack
    } else if (i > toneSamples - decaySamples) {
      envelope = (toneSamples - i) / decaySamples; // linear decay
    }

    // Fundamental + overtone
    const fundamental = Math.sin(2 * Math.PI * tone.freq * t);
    const overtone =
      Math.sin(2 * Math.PI * tone.freq * OVERTONE_RATIO * t) * OVERTONE_GAIN;

    samples[startSample + i] +=
      (fundamental + overtone) * envelope * MASTER_GAIN;
  }
}

// Convert to 16-bit PCM
const pcmData = Buffer.alloc(numSamples * 2);
for (let i = 0; i < numSamples; i++) {
  const clamped = Math.max(-1, Math.min(1, samples[i]));
  const intVal = Math.round(clamped * 32767);
  pcmData.writeInt16LE(intVal, i * 2);
}

// Build WAV file
const dataSize = pcmData.length;
const fileSize = 36 + dataSize;
const header = Buffer.alloc(44);

// RIFF header
header.write('RIFF', 0);
header.writeUInt32LE(fileSize, 4);
header.write('WAVE', 8);

// fmt chunk
header.write('fmt ', 12);
header.writeUInt32LE(16, 16); // chunk size
header.writeUInt16LE(1, 20); // PCM format
header.writeUInt16LE(NUM_CHANNELS, 22);
header.writeUInt32LE(SAMPLE_RATE, 24);
header.writeUInt32LE(SAMPLE_RATE * NUM_CHANNELS * (BITS_PER_SAMPLE / 8), 28); // byte rate
header.writeUInt16LE(NUM_CHANNELS * (BITS_PER_SAMPLE / 8), 32); // block align
header.writeUInt16LE(BITS_PER_SAMPLE, 34);

// data chunk
header.write('data', 36);
header.writeUInt32LE(dataSize, 40);

const wav = Buffer.concat([header, pcmData]);
writeFileSync(OUTPUT_PATH, wav);

const sizeKB = (wav.length / 1024).toFixed(1);
console.log(`Generated ${OUTPUT_PATH} (${sizeKB} KB, ${totalDuration}s)`);
