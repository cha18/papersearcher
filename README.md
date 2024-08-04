# Edexcel Paper Search
Website that allows users to search through indexed edexcel past papers, and returns details of papers that meet query conditions

https://edexcelpapersearch.onrender.com/




** Many past papers are not yet indexed 

I'll probably redo this sometime in the future because its barely held together with very ugly coding practices


---
### Backend
Made up of an API written in Python and a MongoDB database storing paper content and information.

API is hosted on https://pastpaperapi.onrender.com.

#### Usage of API:
  URL parameters:
  * field (required) - property to be queried. `content`, `subject_code` (_subject_code is experimental_).
  * query (required) - string to search for in paper
  * order - order of sorting according to query match score. 1 is ascending, -1 is descending
  * subject - paper's subject
  * subject_code - paper's subject code

### Frontend
Built on Vuejs framework, using Vitejs tooling and tailwindcss.



---



