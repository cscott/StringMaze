#!/usr/bin/python

import mw

# Generators
def root_vegetables():
    return iter(['carrot', 'potato'])

def postal_abbrev_of_US_state():
    return iter(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'])

def metallic_element():
    return iter(['Lithium', 'Sodium', 'Potassium', 'Rubidium', 'Caesium', 'Francium', 'Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium', 'Zinc', 'Molybdenum', 'Cadmium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Yttrium', 'Zirconium', 'Niobium', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Ununbium', 'Aluminium', 'Gallium', 'Indium', 'Tin', 'Thallium', 'Lead', 'Bismuth', 'Ununtrium', 'Ununquadium', 'Ununpentium', 'Ununhexium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium'])

def top_level_domain():
    return iter(['com','info','net','org','biz','name','pro'])

domestic_cat = mw.mw_entry

def month():
    return iter(['January','February','March','April','May','June','July','August','September','October','November','December'])

def zodiac_sign():
    return iter(['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces'])

unit_of_time = mw.mw_entry
surname_of_US_president = mw.mw_entry

def abbrev_of_compass_point():
    return iter(['N','NNE','NE','ENE','E','ESE','SE','SSE',
                 'S','SSW','SW','WSW','W','WNW','NW','NNW'])

def whole_number_in_French():
    return iter(['un','deux','trois','quatre','cinc','six','sept','dix','quinze','seize','vingtetun','cent','mille'])

unit_of_length = mw.mw_entry
#def unit_of_length():
#    pass #

# Implementation of lots of crazy evaluation functions.

cons = set("bcdfghjklmnpqrstvwxyz")
straight = set("aefhiklmntvwxyz")  # uppercase AEFHIKLMNTVWXYZ
first_half = set("abcdefghijklm")
second_half = set("nopqrstuvwxyz")
one_enc = set("adopqr")
two_enc = set("b")
primes = set((2,3,5,7,11,13,17,19,23))

def at_least_three_letters_at_least_twice(s):
    seen = set()
    repeat = set()
    for letter in s:
        if letter in seen:
            repeat.add(letter)
        seen.add(letter)
    return len(repeat)

def number_of_distinct_letters(s):
    return len(set(s))

def number_of_letters(s):
    return len(s)

def even_number_of_letters(s):
    return number_of_letters(s) % 2 == 0

# TODO: has two trigrams that differ by only their middle letter

def in_alphabetical_order(s):
    old = None
    for c in s:
        if c < old:
            return False
        old = c 
    return True

def consonants(s):
    return [x for x in s if x in cons]

def vowels(s):
    return [x for x in s if x not in cons]

def four_consonants(s):
    return len(consonants(s)) == 4

# TODO: contains the name of a board game played on a square grid
# "chess", "battleship", "checkers"
def contains_name_of_board_game_on_square_grid(s):
    return True # XXX

def no_touching_letters_that_are_also_touching_in_the_alphabet(s):
    old = 0
    for i in map(ord, s):
        if i - old == 1 or old - i == 1:
            return False
        old = i
    return True

# TODO: need set called anagrams_of_entries based on letter-level sorted words
# from entries file
def anagram_of_entry(s):
    return mw.is_anagram(s)

def all_different_letters(s):
    return len(set(s)) == len(s)

# TODO: one-letter change away from result at room visited earlier (need
# history)

# TODO: if one character were deleted, would be contain name of a world
# capital

# TODO: clarify if "four different roman numerals" means four characters of
# which each is a Roman numeral, four substrings that parse as Roman
# numerals, or four characters all with distinct values of which is a Roman
# numeral
# (this function uses the first interpretation)
def contains_at_least_four_roman_numerals(s):
    return len([x for x in s if x in "mdclxvi"]) >= 4
 
def is_four_letters_or_shorter(s):
    return len(s) <= 4

def alternates_consonants_and_vowels(s):
    old = s[0] in cons
    for c in s[1:]:
        if (c in cons) is old:
            return False
        old = not old
    return True

# TODO: make sure all the input is always exclusively lowercase
def word_sum(s):
    return sum(map(lambda c: ord(c) - 96, s))

def word_sum_between_60_and_70(s):
    # maybe faster than using a temporary variable and integer comparison?
    # but maybe not
    return word_sum(s) in (60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70)

# TODO: Scrabble score divisible by 9
def scrabble_score_divisible_by_9(s):
    return True # XXX

def straight_line_letters_only(s):
    for c in s:
        if c not in straight:
           return False
    return True

def more_letters_from_second_half(s):
    return len([x for x in s if x in second_half]) > len([x for x in s if x in first_half])

def exactly_one_double(s):
    old = None
    seen = False
    for c in s:
        if c == old:
           if seen:
              return False
           seen = True
        old = c
    return seen

def contains_name_of_Monopoly(s):
    for prop in ['Kentucky','Indiana','Illinois','Chance','Atlantic','Ventnor','Waterworks','Marvin','Pacific','NorthCarolina','CommunityChest','Pennsylvania','ShortLine','Park','Boardwalk','Mediterranean','Baltic','IncomeTax','Reading','Oriental','Vermont','Connecticut','InJail','JustVisiting','StCharles','Electric','States','Virginia','Pennsylvania','StJames','Tennessee','NewYork']:
        if prop.lower() in s: return True
    return False

# TODO: has exactly one letter that appears exactly 3 times
def _count_letters(s):
    r = {}
    for ss in s:
        r[ss] = r.get(ss, 0) + 1
    return r

def one_letter_that_appears_three_times(s):
    tt = [ k for (k,v) in _count_letters(s).iteritems() if v==3]
    return len(tt)==1

def prime_number_of_letters(s):
    return len(s) in primes

# TODO: does not have at least twice as many consonants as vowels

def does_not_have_at_least_twice_as_many_consonants_as_vowels(s):
    print consonants(s), vowels(s)
    return len(consonants(s)) < 2 * len(vowels(s))

def has_exactly_six_enclosed_areas(s):
    return 6 == (len([x for x in s if x in one_enc]) + 2 * len([x for x in s if x in two_enc]))

def has_exactly_nine_distinct_letters(s):
    return 9 == number_of_distinct_letters(s)

def is_entry_at_least_six_long(s):
    return len(s) >= 6 and s in mw._dict_words
