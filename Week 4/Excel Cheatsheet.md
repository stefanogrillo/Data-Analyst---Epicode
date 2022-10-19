# List of Basic Functions

The functions at use can be seen [here](). <br>
The Microsoft's list of function in Alphabetical Order can be found [here](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188#bm4). <br>
The functions and their Italian counterparts can be found [here](https://www.valterborsato.it/Blog%20Posts/FUNZIONI_Excel_ITALIANO_e_INGLESEi.html).


| <b>Function<b> | <b>Explanation<b> |
| -------------- | ----------------- |
| <b>AND(logical1; [logical2]; [logical3]; ...)<b> | Verifies that all the conditions (logical1, logical2, logical3) are simultaneously met. Returns a boolean: _TRUE_ or _FALSE_ |
| <b>AVERAGE(number1;[number2]; ...)<b> | Averages all the numbers selected in the list. Returns a _number_ |
| <b>AVERAGEA(number1;[number2]; ...)<b> | Returns the average of its arguments, including numbers, text, and logical values (counted as 1, except for empty-cells and for FALSE). Returns a _number_ |
| <b>AVERAGEIF(average_range; criteria_range; criteria;)<b> | Averages the range selected, if the criteria_range respects the criteria. Returns a _number_ |
| <b>AVERAGEIFS(average_range; criteria_range1; criteria1; [criteria_range2; criteria2]; ...)<b> | Averages the range selected, if the criteria_range1 respects the criteria1, the criteria_range2 respects the criteria2, etc. Returns a _number_ |
| <b>CHAR(text)<b> | Returns the character (_char_, other) specified by the code number in the ASCII table |
| <b>CONCAT(text1; ...)<b> | Unites text1 with as many other texts as we want. You can also use &. Returns a _string_ |
| <b>COUNT(range)<b> | Counts the cells in the range that are numbers. Returns a _number_ |
| <b>COUNTA(range)<b> | Counts the cells in the range that are not empty. Returns a _number_ |
| <b>COUNTBLANK(range)<b> | Counts the EMPTY cells in the range. Returns a _number_ |
| <b>COUNTIF(range; criteria)<b> | Counts the elements in the range that respect the criteria chosen. Returns a _number_ |
| <b>COUNTIFS(criteria_range1; criteria1; ...)<b> | Counts the elements in the range that respect the criterias chosen. Returns a _number_ |
| <b>DAY(serial_number)<b> | It returns the corresponding day-value from the serial_number. Returns a _number_ |
| <b>DATEDIF(serial_number1;serial_number2;"y")<b> | It calculates the difference between two dates in terms of Years ("y"), Months ("m"), Days ("d"), and mixed "md". Returns a _number_ |
| <b>IF(logical_test; [value_if_true]; [value_if_false])<b> | Checks for the validity of the logical_test. Returns the same format (_number_, _date_, _boolean_, etc) as the value_if_true, or as value_if_false |
| <b>IFERROR(value; value_if_error)<b> | (Perfect for checking _conditionals_ like ISBLANK(value)). It checks if value is TRUE. If not, it returns the value_if_error, that could be of any format (_number_, _date_, _boolean_, etc) |
| <b>INDEX(array; row_num; col_num)<b> | From the table (array), this function returns the value in the absolute row number (row_num) and relative (to the table) column number (col_num). Returns the same format (_number_, _date_, _boolean_, etc) as the data in that column and row |
| <b>ISBLANK(value)<b> | Checks if the value is blank. Returns _TRUE_ or _FALSE_ |
| <b>LEFT(text; [num_chars])<b> | Returns as many chars as specified in num_chars, starting from left, from text. Returns a _string_ | 
| <b>LOWER(text)<b> | Returns a lowercase text as _string_  |
| <b>MATCH(lookup_value; lookup_array; [match_type])<b> | Looks for the lookup_value in the lookup_array, with Exact Match (0), Less Than (1), or Greater Than (-1). Found the data, it returns the corresponding relative (to the table) row number. Returns a _number_ |
| <b>MAX(number1;[number2]; ...)<b> | Finds the greatest value in a list of numbers. Returns a _number_ |
| <b>MID(text; start_num; num_chars)<b> | Extract n chars (num_chars) from the position m (start_num) from the text given. Returns a _string_ |
| <b>MIN(number1;[number2]; ...)<b> | Finds the smallest value in a list of numbers. Returns a _number_ |
| <b>MONTH(serial_number)<b> | It returns the corresponding month-value from the serial_number. Returns a _number_ |
| <b>NETWORKDAYS(start_date; end_date; [holidays])<b> | Calculates the difference between the dates in number of days minus the number of holidays. Returns a _number_ |
| <b>NETWORKDAYS.INTL(start_date; end_date; [weekend]; [holidays])<b> | Calculates the difference between the dates in number of days minus the number of weekend days and the holidays. Returns a _number_ |
| <b>NOT(logical)<b> | Changes TRUE to FALSE, and FALSE to TRUE |
| <b>OR(logical1; [logical2]; [logical3]; ...)<b> | It checks if at least one of the conditions is true. Returns a boolean: _TRUE_ or _FALSE_ |
| <b>PROPER(text)<b> | Returns text, with the first letter as uppercase, as a _string_ |
| <b>REPLACE(old_text; star_num; num_chars; new_text)<b> | This function replaces in the old_text the new_text, instead of the n chars (num_chars) from the starting point (star_num). Returns a _string_ | 
| <b>RIGHT(text; [num_chars])<b> | Returns as many chars as specified in num_chars, starting from right, from text. Returns a _string_ |
| <b>ROUND(number; num_digits)<b> | Rounds the number to a total n digits. Returns a _number_ |
| <b>SUBSTITUTE(text; old_text; new_text; [instance_num])<b> | From text, this functions subtitutes old_text with new_text for n times [instance_num]. Return a _string_ |
| <b>SUM(number1;[number2]; ...)<b> | Sums all the values in the chosen list. Returns a _number_ |
| <b>SUMIF(range; criteria; [sum_range])<b> | Choose a list to check for a criteria. Then choose the range of values to be summed if that criteria is respected. Returns a _number_ |
| <b>SUMIFS(sum_range; criteria_range1; criteria1; ...)<b> | Choose the list of values to be summed. Then select a range of values to be checked for the first criteria. Then repeat the range/criteria selection for as many times as needed. Returns a _number_ |
| <b>TEXT(number)<b> | Formats a number and converts it to text. Returns a _date_ |
| <b>TODAY()<b> | Return the serial number corresponding to today's value. Returns a _number_, except if you check home>number>date, when it returns a value _date_ |
| <b>UPPER(text)<b> | Returns an uppercase text as _string_ |
| <b>VLOOKUP(lookup_value; table_array; col_index_num; [range_lookup]) | Searches for the lookup_value in the range_lookup. When the value is met, it returns the n-th column (col_index_num) from the selected table of data (table_array). Returns the same format (_number_, _date_, _boolean_, etc) as the n-th's column data |
| <b>XLOOKUP(lookup_value; lookup_array; return_array; [if_not_found]; [match_mode]; [search_mode])<b> | This function looks for the lookup_value in the lookup_array. It returns the corresponding values (in terms of row) from the return_array, or a chosen answer ([if_not_found]) if the lookup_value is not found. It allows 4 match modes, exact is 0. Allows for 4 search modes, with first-to-last being 1. Returns the same format (_number_, _date_, _boolean_, etc) as the return_array columns' data |
| <b>YEAR(serial_number)<b> | It returns the corresponding year-value from the serial_number. Returns a _number_ |
| <b>YEARFRAC(serial_number1; serial_number2; [basis])<b> | It returns the corresponding year-value from the difference between serial_number1 and serial_number2. The [basis] indicates 4 possibilities: 30/360, actual/actual, actual/360, actual/365, 30/360. Returns a _number_ |
| <b>XOR(logical1; [logical2]; ...)<b> | Returns a logical exclusive OR of all arguments. If more than one OR are met, gives FALSE. Returns boolean: TRUE or FALSE |
| <b>WEEKNUM(serial_number; [return_type])<b> | Returns the number of weeks, counting a week from the return_type. Returns a _number_ |


| <b>Operations<b> | <b>How to<b> |
| ---- | ---- |
| <b>Operators<b> | +  -  /  *  ^  %  |
| <b>Logical Operators<b> | =  <  >  >=  <=  <> (the last indicates "difference") |
| <b>Other<b> | ? * (can be used as in SQL to indicate 1 char of any type, or any amount of chars of any type) |
| <b>Interval & Union<b> | : ; |
| <b>Number of days/months/years between two dates<b> | = DATEDIF(serial_number1; serial_number2; "y") |
| <b>Number of years<b> | =INT((TODAY() - serial_number)/365,25) |
| <b>Years, Months, Days from a date<b> | =(YEAR(TODAY())-YEAR(serial_number))&" ANNI "&(MONTH(TODAY())-MONTH(serial_number))&" MESI "&(DAY(TODAY()) - DAY(serial_number))&" GIORNI" |
| <b>Add X days to a date<b> | = serial_number + X |
| <b>Only the last word between two<b> | =RIGHT(C32;LEN(C32)-SEARCH(" ";C32)) |
| <b>Only the first word between two<b> | =LEFT(B17; SEARCH(" ";B17;1)-1) |
| <b>Text format for today's date<b> | TEXT(TODAY();) |
