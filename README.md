# Material PySide

[![Join the chat at https://gitter.im/IronManMark20/Material](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/IronManMark20/Material?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

^^ I am often on Gitter so you will find me there.

#NO LONGER SUPPORTED, but feel free to ask questions on the gitter. I might answer them.

A collection of PySide Widgets for theming applications to give a material design look.

Currently, only PySide for Qt4 is working. Python 2.7 and 3.x works!

Currently, the following widgets are supported (not all implemented right now):

- LineEdit - implemented
- TextEdit - not implemented (v0.2)
- PushButton - FAB, Raised and Flat
- TabBar - implemented
- ListView - implemented
- ProgressBar - implemented
- Checkbox - implemented
- TopBar - implemented
- Dialog - not implemented (v0.2)

QPushButton has 3 styles: Flat, Raised, and Floating Action. To read more on these styles [read the button spec](http://www.google.com/design/spec/components/buttons.html).

Also, I have added a custom Text class which uses Roboto font as a bonus.

#Install

simple! run `git clone https://github.com/IronManMark20/material.git && cd material`


##Example
To see the example, run the `example.py` file. It will give you an example application.

Also, the wiki will (in the future) have documentation for each widget. To start though, you can read through the source of `example.py` for examples.


#Screenshots

First page with list view:
![first page](http://i.imgur.com/dkeez6g.png)

and seccond page

![second page](http://i.imgur.com/yTsnZpE.png)

#Contributing

I take pull requests! Let me know if you are interested in contributing. The best way would be to open a new issue with the widget or fix you are going to work on. Fork the project, and push commits to that. Then, when you are done, you can make a pull request. I will check the changes you made and either approve it, or explain how it can be fixed. 

###Note:
By making a pull request, you agree that the code you are commiting is released under the LGPL.

#License

All of the *.qss files and *.py are [LGPL v3](https://www.gnu.org/licenses/lgpl.txt) licensed, and the *.SVG images are released under [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

