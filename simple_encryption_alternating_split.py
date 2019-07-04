from itertools import chain, islice, zip_longest

from codewars_test import Test


def encrypt(text, n):
    for _ in range(n):
        text = ''.join(chain(islice(text, 1, len(text), 2), islice(text, 0, len(text), 2)))
    return text


def decrypt(encrypted_text, n):
    t = encrypted_text
    for _ in range(n):
        t = ''.join(chain(*zip_longest(t[len(t) // 2:], t[:len(t) // 2], fillvalue='')))
    return t


Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
Test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

Test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
Test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
Test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
Test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
Test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
Test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
Test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

Test.assert_equals(encrypt("", 0), "")
Test.assert_equals(decrypt("", 0), "")
Test.assert_equals(encrypt(None, 0), None)
Test.assert_equals(decrypt(None, 0), None)
