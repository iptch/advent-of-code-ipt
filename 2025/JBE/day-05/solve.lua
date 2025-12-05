local io = require("io")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function contains(range, val)
  return val >= range.low and val <= range.high
end

local function contained(range1, range2)
  return contains(range2, range1.low) and contains(range2, range1.high)
end

local function part_1()
  local ranges = {}
  local ids = {}
  for line in io.lines(inputfile) do
    local s, e = line:match("(%d+)%-(%d+)")
    if s then
      ranges[#ranges + 1] = { low = tonumber(s), high = tonumber(e) }
    elseif line ~= "" then
      ids[#ids + 1] = tonumber(line)
    end
  end
  local res = 0
  for _, id in ipairs(ids) do
    for _, range in ipairs(ranges) do
      if contains(range, id) then
        res = res + 1
        break
      end
    end
  end
  return res
end

local function part_2()
  local ranges = {}
  for line in io.lines(inputfile) do
    local s, e = line:match("(%d+)%-(%d+)")
    if s then
      local tmp = { low = tonumber(s), high = tonumber(e) }
      local skip = false
      local new_ranges = {}
      for _, range in ipairs(ranges) do
        if contained(tmp, range) then
          new_ranges[#new_ranges + 1] = range
          skip = true
        elseif contains(range, tmp.low) then
          new_ranges[#new_ranges + 1] = range
          tmp.low = range.high + 1
        elseif contains(range, tmp.high) then
          new_ranges[#new_ranges + 1] = range
          tmp.high = range.low - 1
        elseif not contained(range, tmp) then
          new_ranges[#new_ranges + 1] = range
        end
      end
      if not skip and tmp.low <= tmp.high then
        new_ranges[#new_ranges + 1] = tmp
      end
      ranges = new_ranges
    end
  end
  local res = 0
  for _, range in ipairs(ranges) do
    res = res + (range.high - range.low + 1)
  end
  return res
end

local function main()
  local p1 = part_1()
  print(string.format("Part 1: %15d", p1))
  local p2 = part_2()
  print(string.format("Part 2: %15d", p2))
end

main()
