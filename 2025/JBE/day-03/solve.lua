local io = require("io")

local inputfile = arg[1] == "test" and "example.txt" or "input.txt"

local function solve(length)
  local sum = 0
  for line in io.lines(inputfile) do
    local digits = {}
    for idx = 1, length do
      digits[idx] = 0
    end
    for idx = 1, #line - length + 1 do
      local test = {}
      for dig = 1, length do
        test[dig] = tonumber(line:sub(idx + dig - 1, idx + dig - 1))
      end
      for j = 1, length do
        if test[j] > digits[j] then
          for z = j, length do
            digits[z] = test[z]
          end
          break
        end
      end
    end
    local val = table.concat(digits)
    sum = sum + tonumber(val)
  end
  return sum
end

local function main()
  local p1 = solve(2)
  print(string.format("Part 1: %15d", p1))
  local p2 = solve(12)
  print(string.format("Part 2: %15d", p2))
end

main()
