local io = require("io")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function part_1()
  local fh = assert(io.open(inputfile, "r"))
  local content = fh:read("*a")
  fh:close()
  local sum = 0
  for rstart, rend in content:gmatch("(%d+)%-(%d+)") do
    for val = tonumber(rstart), tonumber(rend) do
      local tval = tostring(val)
      if #tval % 2 == 0 then
        local middle = #tval / 2
        if tval:sub(1, middle) == tval:sub(-middle) then
          sum = sum + val
        end
      end
    end
  end
  return sum
end

local function range_sum(rstart, rend)
  local sum = 0
  for val = tonumber(rstart), tonumber(rend) do
    local tval = tostring(val)
    for cur = 1, #tval / 2 do
      local tester = tval:sub(1, cur)
      local found = true
      for idx = cur + 1, #tval, cur do
        if tval:sub(idx, idx + cur - 1) ~= tester then
          found = false
        end
      end
      if found then
        sum = sum + val
        break
      end
    end
  end
  return sum
end

local function part_2()
  local fh = assert(io.open(inputfile, "r"))
  local content = fh:read("*a")
  fh:close()
  local sum = 0
  for rstart, rend in content:gmatch("(%d+)%-(%d+)") do
    sum = sum + range_sum(rstart, rend)
  end
  return sum
end

local function main()
  local p1 = part_1()
  print("Part 1:", p1)
  local p2 = part_2()
  print("Part 2:", p2)
end

main()
