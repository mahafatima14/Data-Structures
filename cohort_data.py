"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    cohort_data = open(filename)
    for line in cohort_data:                          #iterate over each line in the filecd
      line = line.rstrip()                            #remove right white space
      student_data = line.split("|")                  #split each line by |
      house = student_data[2]                         #assign house to data at index 2
      if house != "":                                 #if house is not blank, add house to set
        houses.add(house)

    return houses


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    cohort_data = open(filename)
    for line in cohort_data:
      line = line.rstrip()                              #remove right white space
      student_data = line.split("|")                    #split each line by |
      first_name = student_data[0]                      #assign first name variable
      last_name = student_data[1]                       #assign last name variable
      full_name = f"{first_name} {last_name}"           #assign full name variable

      if cohort == "All":
        if student_data[4] != "I" and student_data[4] != "G":
          students.append(full_name)
      else:
        if cohort == student_data[4]:
          students.append(full_name)


    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    cohort_data = open(filename)
    for line in cohort_data:
      line = line.rstrip() # remove right white space
      student_data = line.split("|") # split each line by |
      first_name = student_data[0] # assign first name variable
      last_name = student_data[1] # assign last name variable
      full_name = f"{first_name} {last_name}" # assign full name variable
      if student_data[2] == "Dumbledore's Army":
        dumbledores_army.append(full_name)
      elif student_data[2] == "Gryffindor":
        gryffindor.append(full_name)
      elif student_data[2] == "Hufflepuff":
        hufflepuff.append(full_name)
      elif student_data[2] == "Ravenclaw":
        ravenclaw.append(full_name)
      elif student_data[2] == "Slytherin":
        slytherin.append(full_name)
      elif student_data[4] == "G":
        ghosts.append(full_name)
      elif student_data[4] == "I":
        instructors.append(full_name)

    return [sorted(dumbledores_army),sorted(gryffindor),sorted(hufflepuff),sorted(ravenclaw),sorted(slytherin),sorted(ghosts),sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    cohort_data = open(filename)
    for line in cohort_data:
      line = line.rstrip() # remove right white space
      student_data = line.split("|") # split each line by |
      first_name = student_data[0] # assign first name variable
      last_name = student_data[1] # assign last name variable
      full_name = f"{first_name} {last_name}" # assign full name variable
      house = student_data[2]
      advisor = student_data[3]
      cohort = student_data[4]
      all_data.append((full_name, house, advisor, cohort))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    cohort_data = open(filename)
    for line in cohort_data:
      line = line.rstrip() # remove right white space
      student_data = line.split("|") # split each line by |
      first_name = student_data[0] # assign first name variable
      last_name = student_data[1] # assign last name variable
      full_name = f"{first_name} {last_name}" # assign full name variable
      if full_name == name:
        return student_data[4]


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    all_last_names = []
    duplicate_last_names = set()

    cohort_data = open(filename)
    for line in cohort_data:
      line = line.rstrip() # remove right white space
      student_data = line.split("|") # split each line by |
      last_name = student_data[1] # assign last name variable

      if last_name not in all_last_names:
        all_last_names.append(last_name)
      else:
        duplicate_last_names.add(last_name)

    return duplicate_last_names



def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py",
        report=False,
        optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE),
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")
