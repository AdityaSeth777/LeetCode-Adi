int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
  int* out = malloc(2 * sizeof(*out));
  *returnSize = 2;

  const size_t table_size = numsSize * 2;
  struct {
    int val;
    size_t i;
    bool filled;
  } table[table_size];
  memset(&table, 0, sizeof(table));

  for (size_t i = 0; i < numsSize; ++i) {
    const int compliment = target - nums[i];

    size_t bucket = (size_t)compliment * 31337 % table_size;
    while (table[bucket].filled) {
      if (table[bucket].val == compliment && table[bucket].i != i) {
        out[0] = i;
        out[1] = table[bucket].i;
        return out;
      }

      ++bucket;
      if (bucket == table_size) {
        bucket = 0;
      }
    }

    bucket = (size_t)nums[i] * 31337 % table_size;
    while (table[bucket].filled) {
      ++bucket;
      if (bucket == table_size) {
        bucket = 0;
      }
    }

    table[bucket].val = nums[i];
    table[bucket].i = i;
    table[bucket].filled = true;
  }

  return out;
}