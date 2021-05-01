# Text-Analysis-School-Project
This is the python code for the first project for CST2101: Business Intelligence Programming.

The goal of the project was to take a text file - in this case, novels from Project Gutenburg - and produce an analysis (described below). A few sample novels are included.

### Classes

The Program is split into three classes: TextProcessor, FileProcessor, and Helper. The first two are both meant to be used as “tool boxes” for processing text files and producing the required output. The last is meant to supply helper functions to the others. They are all composed entirely of static methods.

**FileProcessor**

This class has two methods. The first, getInput(), is laid out as follows:

*	Prompts the user for a file path;
*	Processes the name of the file path into a usable string, depending on Windows or Unix paths;
*	Checks if the user would like to exit the program;
*	Tries to open the file; throws an exception if it does not exist;
*	If the file exists, it splits its contents into a list of lines;
*	Finally, returns a tuple of the text as a list, and of the filename as a string;

The second, produceOutput(), is laid out as follows:

*	Names the output file according to project specs;
*	Extracts the name of the novel;
*	Writes the analysis file using the TextProcessor methods;
*	Notifies the user when it’s complete.

**TextProcessor**

This class contains all the methods required for doing the analysis required by the specs. They all accept lists of strings as inputs, where the list is meant to be composed of the lines in a text file. 

*	countWords(), countChars() and countSpaces() use simple list comprehensions and return integer values of what they are meant to be counting;
*	proportionSpaces() uses similar list comprehensions to countChars() and countSpaces() and returns the percentage, as a float 
*	wordOccurences() and wordOccurencesSorted() both iterate through the list, and add the words to a dictionary, with value=1 if they are new words or incrementing the value if they are already present. Both methods account for whitespace on the ends and for duplicates because of mismatched cases.

**Helper**

Finally, helper is a class for helper methods for the above two classes. Incase the project functionality  needs to be expanded, this class can be used for other methods as well. 

The method getNovelName() splits the name of the text file by capital letters using regular expressions. It then removes the trailing ‘clean’ or ‘removed’, since the text files, in the context of this project, were preprocessed in this way.

The method getDocsDirectory() returns a string value of the path to the user Documents directory.

### Logic

The code is entirely self-contained in the Processor.py file. It simply calls the two functions in FileProcessor sequentially, which retrieve the input and produce the analysis. As described above, the FileProcessor.produceOutput() method calls methods from TextProcessor, that are used for the analysis required by the project specifications.

The file uses a main guard in case the classes are being used by another file.

All of the analysis files are saved to the users Documents directory: C:\Users\<username>\Documents

### Possible Updates
1. The project spec required "cleaning" novels in advance - i.e., removing the header documentation from the project Gutenburg text file, and the table of contents. I may implement some functionality to remove that automatically.
2. Implementing some web scraping to download a novel of the user's choosing automatically.

