
with open("/Users/jkoziol/Downloads/input.txt") as f:
    records = f.readlines()
    records = [line.rstrip() for line in records]

# records_columns = zip(*records)
# <---- 1st task ---->
# half_column = len(records_columns[0])/2
# gamma_code = ["1" if binary.count("1") > half_column else "0" for binary in records_columns]
# gamma_code = ''.join(gamma_code)
# print(gamma_code)
# gamma_int = int(gamma_code, 2)
# sigma_code = ''.join(["1" if b == "0" else "0" for b in gamma_code])
# print(sigma_code)
# sigma_int = int(sigma_code, 2)

# test
# records = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

filtered_records = records
for idx in range(len(records[0])):
    common_bit = "1" if list(zip(*filtered_records))[idx].count("1") >= list(zip(*filtered_records))[idx].count("0") else "0"
    filtered_records = filter(lambda bin_s: bin_s[idx] == common_bit, filtered_records)
    if len(filtered_records) == 1:
        break
print(filtered_records)
oxygen = int(filtered_records[0], 2)
filtered_records = records
for idx in range(len(records[0])):
    common_bit = "0" if list(zip(*filtered_records))[idx].count("0") <= list(zip(*filtered_records))[idx].count("1") else "1"
    filtered_records = filter(lambda bin_s: bin_s[idx] == common_bit, filtered_records)
    if len(filtered_records) == 1:
        break
co2 = int(filtered_records[0], 2)
print(filtered_records)
print(oxygen * co2)
