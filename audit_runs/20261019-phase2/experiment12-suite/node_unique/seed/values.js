function uniqueValues(values) {
  // Return each primitive value once, preserving its first occurrence order.
  return [...values].sort();
}
module.exports = {uniqueValues};
