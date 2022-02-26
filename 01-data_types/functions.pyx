def information(job):
  cdef str name = "salar"
  cdef unsigned int continent_index = 0
  cdef unsigned int age = 16
  cdef float height = 1.8
  cdef long total_debt = 10_000_000
  cdef int credit = -60_000
  cdef float weight = 82
  cdef bint man = True
  cdef bint woman = False
  return {"name": name, "age": age, "job": job}