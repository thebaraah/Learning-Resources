function fft(x) {
  const N = x.length;
  if (N <= 1) return x;

  // Divide
  const even = [];
  const odd = [];
  for (let i = 0; i < N; i++) {
    if (i % 2 === 0) {
      even.push(x[i]);
    } else {
      odd.push(x[i]);
    }
  }

  // Conquer
  const evenFFT = fft(even);
  const oddFFT = fft(odd);

  // Combine
  const result = new Array(N);
  for (let k = 0; k < N / 2; k++) {
    const t = { real: 0, imag: 0 };
    const angle = -2 * Math.PI * k / N;

    // Complex multiplication: oddFFT[k] * e^(-2πik/N)
    t.real = oddFFT[k].real * Math.cos(angle) - oddFFT[k].imag * Math.sin(angle);
    t.imag = oddFFT[k].real * Math.sin(angle) + oddFFT[k].imag * Math.cos(angle);

    result[k] = {
      real: evenFFT[k].real + t.real,
      imag: evenFFT[k].imag + t.imag
    };

    result[k + N / 2] = {
      real: evenFFT[k].real - t.real,
      imag: evenFFT[k].imag - t.imag
    };
  }

  return result;
}

// Helper function to convert real numbers to complex
function realToComplex(realArray) {
  return realArray.map(val => ({ real: val, imag: 0 }));
}

// Example usage
const input = [1, 2, 3, 4, 0, 0, 0, 0];
const complexInput = realToComplex(input);
const result = fft(complexInput);
console.log("FFT Result:", result);
