## USAGE<br>
1. Clone the repository<br>
```text
      git clone [repository link]
```
2. Navigate to the directory containing the script<br>
```text
      cd [repository_directory]
```
3. Run the script<br>
```text
      python brutethrash.py
```
4. Enter the target website URL when prompted.<br><br>
## MODULES<br>
  * requests : Used for making HTTP requests to the target website.<br>
  * itertools : Provides functions for creating iterators for efficient looping.<br><br>

## SCRIPT STRUCTURE <br>
**try_bruteforce(url, path, user, password)** <br>
* Attempts to authenticate using the provided username and password on the specified URL and path.<br>
* If successful (HTTP status code 200), it prints a success message.<br><br>

**bruteforce(url, path, chars, min_len, max_len)** <br>
* Iterates over all possible combinations of characters within the specified length range.<br>
* Calls try_bruteforce to attempt login with each combination.
