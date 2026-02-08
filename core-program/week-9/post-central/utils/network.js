import os from 'os';

export const getLocalIP = () => {
  const interfaces = os.networkInterfaces();

  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      // Skip internal (loopback) and non-IPv4 addresses
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return 'localhost';
};

export const getIP4Address = (ip) => {
  if (ip.startsWith('::ffff:')) {
    return ip.substring(7);
  }
  return ip;
};
