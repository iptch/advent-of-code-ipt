local io = require("io")
local string = require("string")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function reduce(tbl, op)
  if #tbl < 2 then
    return tbl[1]
  end
  local init = tbl[1]
  for i = 2, #tbl do
    init = op(init, tbl[i])
  end
  return init
end

local function for_each_op(ops_line, func)
  local res = 0
  local idx = 1
  for op in ops_line:gmatch("[^%s]") do
    local operation = function(a, b)
      return a + b
    end
    if op == "*" then
      operation = function(a, b)
        return a * b
      end
    end

    res = res + func(idx, operation)
    idx = idx + 1
  end
  return res
end

local function part_1()
  local values = {}
  local line_nr = 1
  local last_line = ""
  for line in io.lines(inputfile) do
    for number in line:gmatch("(%d+)") do
      if not values[line_nr] then
        values[line_nr] = {}
      end
      values[line_nr][#values[line_nr] + 1] = tonumber(number)
    end
    line_nr = line_nr + 1
    last_line = line
  end

  return for_each_op(last_line, function(idx, op)
    local vals = {}
    for _, row in ipairs(values) do
      vals[#vals + 1] = row[idx]
    end
    return reduce(vals, op)
  end)
end

local function get_op_indexes(ops)
  local res = {}
  local idx = 0
  while idx do
    idx, _ = ops:find("[%+%*]", idx + 1)
    res[#res + 1] = idx
  end
  res[#res + 1] = ops:len() + 1
  return res
end

local function part_2()
  local last_line = ""
  for line in io.lines(inputfile) do
    last_line = line
  end
  local op_idxs = get_op_indexes(last_line)
  local nums = {}
  local line_nr = 1
  for line in io.lines(inputfile) do
    if not nums[line_nr] then
      nums[line_nr] = {}
    end
    for idx = 1, #op_idxs - 1 do
      local start = op_idxs[idx]
      local stop = op_idxs[idx + 1]
      nums[line_nr][#nums[line_nr] + 1] = line:sub(start, stop - 1)
    end
    line_nr = line_nr + 1
  end
  nums[#nums] = nil -- discard last line

  return for_each_op(last_line, function(idx, op)
    local vals = {}
    for j = 1, nums[1][idx]:len() do
      local val = ""
      for _, row in ipairs(nums) do
        val = val .. row[idx]:sub(j, j)
      end
      if val ~= "" then
        vals[#vals + 1] = tonumber(val:match("%d+"))
      end
    end
    return reduce(vals, op)
  end)
end

local function main()
  local p1 = part_1()
  print(string.format("Part 1: %15d", p1))
  local p2 = part_2()
  print(string.format("Part 2: %15d", p2))
end

main()
