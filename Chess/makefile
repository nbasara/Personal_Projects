JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java
CLASSES = Game.java Board.java Player.java Pieces.java

default: classes

classes: $(CLASSES:.java=.class)

clean: 
	$(RM) *.class
