# CourseGrammar-Source-Code
CourseGrammar is the source code of the Grammar written using Gold Parser. This is the grammar we have created in the course in Udmey called # Programming Languages + Build an Interpreter. The grammar is created using Gold Parser which allows you to write any or describe grammar of programming languages using BNF mate Language.

<Main> ::= program begin: <Statements> end
<Main> is where the grammar starts from. program, begin, :, and end are keywords of the prgramming language grammar. <Statements> is...
<Statements> ::= <Statement> |<Statement> <Statements> either one statement or mult-statements. We describe statement as followed...
<Statement> ::= <Expression>
             | <VariableDeclarators>
             | <Condition>
             | <Loops>
             | <Counters>
             | <DataType>
             | <MethodDeclaration>
             | <MethodCall>
             | <Array>
             | <Print>
             | <input>
  
We of these non-terminal is a part of the language. <Expression> is no thing more than arithmtic expression and so on. All these non-teminal above are described in CourseGrammar.grm in details. The mate langaue I used to write the synatx of the grammar is called BNF. It's only used either to describe an existing prgramming language or write a new grammar for new prgramming language.
# CourseGrammar-Source-Code
