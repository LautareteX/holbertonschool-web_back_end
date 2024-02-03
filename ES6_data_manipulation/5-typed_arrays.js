export default function createInt8TypedArray(len, pos, val) {
  if (pos < 0 || pos > len) {
    throw new Error('Posición fuera de rango');
  }
  const buf = new ArrayBuffer(len);
  const arr = new Int8Array(buf);
  const view = new DataView(buf);
  arr[pos] = val;
  return view;
}
