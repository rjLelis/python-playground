import string_utils

assert 'rento' == string_utils.remove_special_char('ren@to'), 'remove_special_char .... FAILED'
print('remove_special_char .... SUCCESS')

assert 'otaner' == string_utils.reverse('renato'), 'reverse .... FAILED'
print('reverse .... SUCCESS')

assert string_utils.is_palindrome('ana'), 'is_palindrome .... FAILED'
print('is_palindrome .... SUCCESS')