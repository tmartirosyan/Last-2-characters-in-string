sample_string = "excercises"
string_last_2_copied_4_times = sample_string[-2:] * 4
print(string_last_2_copied_4_times)


# solution version 2 (with function)
def Get_last_2_chars_and_copy_4_times(sample_string) :
    if len(sample_string) >= 2 :
        return sample_string[-2:] * 4
    return "Your text must be longer than 2 characters"

print(Get_last_2_chars_and_copy_4_times("n"))