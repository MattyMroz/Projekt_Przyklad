========== Variables And Data Types ==========
Byte 	    0 do 255
Boolean     True lub False
Integer 	-32,768 do +32,767
Long        -2,147,483,648 do +2,147,483,647
Single      -3.4e38 do +3.4e38
Double      -1.8e308 do +1.8e308
Currency    -922,337,203,685,477.5808 do +922,337,203,685,477.5807
Date 	    1 styczeń 100 to 31 grudzień 9999
Object      wskaźnik na dowolny obiekt
String      Zmienny – Do 2 bilionów znaków
Variant     Może przechowywać dowolną z powyższych wartości
==========

                            
                            
                            
========== Deklaracja zmiennych ==========
Dim intAge As Integer, strText As String, Variant As Variant
intAge = 35
strText = "I am " & intAge & " years old."
Variant = strText
==========

                            
                            
                            
========== Przypisywanie wartości do obiektów ==========
' txt i btn
Private Sub btnGo_Click()
    Dim strText As String
    strText = "Hello World!"
    txtOutput.Value = strText
End Sub
==========

                                
                                
                                
========== If Statement ==========
' checkbox i btn
Private Sub btnGo_Click()
   Dim YesNo As Boolean
'    =,<>,>,<,>=,<=, And, Or, Not (If Not)
    If ThkYesNo = False Then
        YesNo = True
        MsgBox"True!"
   Else
        YesNo = False
        MsgBox"False!"
   End If
   ThkYesNo = YesNo
End Sub
                                    
==============================

If IsNull(Me![nazwa_pola]) Then
      instrukcje
   Else
instrukcje
End If

==========

                                    
                                    
                                    
==========  Select Case ==========
Private Sub btnGo_Click()
    Dim x As Integer
    x = Me.txtNumber.Value

    Select Case True
    Case x < 9
        MsgBox "x is less than 9"
    Case x >= 9 And x < 20
        MsgBox "x is between 9 and 20"
    Case x >= 20 And x < 29
        MsgBox "x is between 20 and 29"
    Case Else
        MsgBox "x is greater than 29"
    End Select
End Sub
==========

                                        
                                        
                                        
========== Looping Statements ==========
Private Sub btnGo_Click()
    Dim x As Integer
    Dim y As Integer
    Dim strMessage As String
    x = Me.txtNumber.Value
    strMessage = ""

    y = 0
    Do While y < x
        strMessage = strMessage & y & " "
        y = y + 1
    Loop

    y = 0
    Do
        strMessage = strMessage & y & " "
        y = y + 1
    Loop While y < x

    y = 0
    Do Until y = x
        strMessage = strMessage & y & " "
        y = y + 1
    Loop

    For y = 0 To x Step 2
        strMessage = strMessage & y & " "
    Next

    Dim a(2) As Integer
    Dim b As Variant

    For y = 0 To 2
        a(y) = y 'zapisywanie wartości do tablicy
    Next y

    For Each b In a
        strMessage = strMessage & b & " "
    Next

    Me.txtOutput.Value = strMessage
    MsgBox strMessage
End Sub
==========

                                
                                
                                

========== Frames and Arithmetic ==========
Private Sub btnGo_Click()
    Dim x As Double
    Dim y As Double
    Dim result As Double
    x = Me.txtNumber.Value
    y = Me.txtNumber2.Value

    Select Case Me.fraMath 'ramka wyboru
        Case Is = 1
            result = x + y
        Case Is = 2
            result = x - y
        Case Is = 3
            result = x * y
        Case Is = 4
            result = x \ y
        Case Is = 5
            result = x / y
        Case Is = 6
            result = x ^ y
        Case Else
            result = x Mod y
   End Select
   Me.txtResult = result
End Sub
==========
                                
                                
                                
                                
========== Array ==========
Private Sub btnGo_Click()
    Dim text As String
    Dim output As String
    Dim item As Variant

    ' Fill a string with data which is semi-colon delimited
    text = "1;2;3"

    ' Dim the array
    Dim Numbers() As String '<-- Dynamic Array

    ' Split the text and put it into the dynamic array
    Numbers() = Split(text, ";")
    For Each item In Numbers
        MsgBox item
    Next
    output = Join(Numbers, ",")
    MsgBox output

    ' ReDim to change the subscript range
    ReDim Preserve Numbers(4) '<-- Same as "ReDim Preserve Numbers(0 To 4)
    Numbers(3) = 4
    Numbers(4) = 5

    MsgBox Join(Numbers, ",")

    ' Using LBound and UBound to determine the Lower and Upper subscript boundaries
    Dim i As Integer
    For i = LBound(Numbers()) To UBound(Numbers())
        Numbers(i) = i
    Next i
    MsgBox Join(Numbers, ",")


    '==============================
    '== Multi-Dimensional Arrays ==
    '==============================
    Dim tableOfNums(4, 4) As String '<-- Static Array

    ' Fill the array with X and Y values
    Dim x, y As Integer
    For x = 0 To 4
        For y = 0 To 4
            tableOfNums(x, y) = "X=" & x & " Y=" & y
        Next
    Next

    ' Fill table with data from array for better visualization
    Dim rs As Recordset
    Dim xbound, ybound As Integer
    Set rs = CurrentDb.OpenRecordset("tbl1Output", dbOpenDynaset, dbSeeChanges)
    xbound = UBound(tableOfNums, 1)
    ybound = UBound(tableOfNums, 2)
    For x = 0 To xbound
        With rs
            .AddNew
            For y = 0 To ybound
                .Fields(y) = tableOfNums(x, y)
            Next
            .Update
        End With
    Next

    'Open the Output table
    DoCmd.OpenTable "tbl1Output", acViewNormal
    Stop

    'Run this command to delete the data from tbl1Output
    CurrentDb.Execute "DELETE * from tbl1Output"

End Sub
==========

            
            
            
========== Login Screen ==========
Private Sub btnLogin_Click()
    Dim strCBOPass As String
    Dim strPassword As String

    strCBOPass = Me.cboUsername.Column(1)
    strPassword = Me.txtPassword

    If strCBOPass = strPassword Then
        MsgBox "Login Successful!"
    Else
        MsgBox "Login Unsuccessful!"
    End If
End Sub
==========

            
            
            
========== Debugging and Error Handling ==========
            
           View > Immediate Window > ?err.Number = wyświetlenie numeru błędu 
            
Private Sub btnGo_Click()
    On Error GoTo problem
    MsgBox "Answer:" & (Me.txtValuel / Me.txtValue2)
    Exit Sub

problem:
    If Err.Number = 11 Then ' błąd dzielenia przez zero sprawdzanie przy wywołaniu funkcji
        MsgBox "Cannot Divide By Zero"
    Else
        MsgBox "Please enteravalid number"
    End If
End Sub
==========


Otworzenie nowego formularza z odpowiednim id
                
Private Sub btnOpenTowary_Click()
    On Error GoTo problem

    DoCmd.OpenForm "towary", , , "[IDtowar]=" & Me![Lista6]
    Exit Sub
    
problem:
    MsgBox "Zaznacz poprawnie"
End Sub
                
==========

                
                
                
========== Functions and Subroutines ==========
Dim Operator As String

Private Sub btnAdd_Click()
    Operator = "+"
    Math
End Sub

Private Sub btnDiv_Click()
    Operator = "/"
    Math
End Sub

Private Sub btnMul_Click()
    Operator = "*"
    Math
End Sub

Private Sub btnSub_Click()
    Operator = "-"
    Math
End Sub

Private Sub Math()
    On Error GoTo Problem

    Select Case Operator
        Case Is = "+"
            MsgBox CDbl(Me.txtValue1) + CDbl(Me.txtValue2)
        Case Is = "-"
            MsgBox Me.txtValue1 - Me.txtValue2
        Case Is = "*"
            MsgBox Me.txtValue1 * Me.txtValue2
        Case Is = "/"
            MsgBox Me.txtValue1 / Me.txtValue2
    End Select

    Exit Sub

Problem:
    Select Case Err.Number
        Case Is = 11
            MsgBox "Cannot divide by Zero."
        Case Is = 13
            MsgBox "Both values must be numeric."
        Case Else
            MsgBox "Could not perform function.  Please try again."
    End Select
End Sub
==========

                    
                    
                    
========== Passing Arguments to Parameters ==========
Option Compare Database
Option Explicit

Dim Operator As String

Private Sub btnAdd_Click()
    Operator = "+"
    MsgBox Calculation(Operator, Me.txtValue1, Me.txtValue2)
    Debug.Print Operator
End Sub

Private Sub btnDiv_Click()
    Operator = "/"
    MsgBox Calculation(Operator, Me.txtValue1, Me.txtValue2)
    Debug.Print Operator
End Sub

Private Sub btnMul_Click()
    Operator = "*"
    MsgBox Calculation(Operator, Me.txtValue1, Me.txtValue2)
    Debug.Print Operator
End Sub

Private Sub btnSub_Click()
    Operator = "-"
    MsgBox Calculation(Operator, Me.txtValue1, Me.txtValue2)
    Debug.Print Operator
End Sub

Private Function Calculation(Op As String, Value1 As Double, Value2 As Double) As Double
    On Error GoTo Problem

    Select Case Op
        Case Is = "+"
            Calculation = Value1 + Value2
        Case Is = "-"
            Calculation = Value1 - Value2
        Case Is = "*"
            Calculation = Value1 * Value2
        Case Is = "/"
            Calculation = Value1 / Value2
    End Select
    Op = "Something Else"
    Exit Function

Problem:
    Select Case Err.Number
        Case Is = 11
            MsgBox "Cannot divide by Zero."
        Case Is = 13
            MsgBox "Both values must be numeric."
        Case Else
            MsgBox "Could not perform function.  Please try again."
    End Select
End Function
==========

========== 39 VBA - Access Modifiers ==========

                        
                        
                        
========== DoCmd ==========
Private Sub btnAdd_Click()
    Me.AllowAdditions = True
    DoCmd.GoToRecord , , acNewRec
    Me.txtUserName = "     "
    Me.AllowAdditions = False
End Sub

Private Sub btnBack_Click()
    DoCmd.GoToRecord , , acPrevious
End Sub

Private Sub btnExample_Click()
'    DoCmd.Beep
'    DoCmd.BrowseTo acBrowseToForm, "frmForm"
'    DoCmd.OpenForm "frmForm"
'    DoCmd.Close acForm, "frmEmployees"
'    DoCmd.GoToControl "txtFirstName"
'    DoCmd.Hourglass True
'    DoCmd.Maximize
'    DoCmd.Minimize
'    DoCmd.Restore
'    DoCmd.OpenReport "Report1", acViewPreview
'    DoCmd.OutputTo acOutputReport, "Report1", acFormatPDF, "c:\test\test.pdf", True
'    DoCmd.OutputTo acOutputTable, "tbl1Employees", , "c:\test\test.xls", True
'    DoCmd.Quit
'    DoCmd.RefreshRecord
'    DoCmd.Requery Me.Name
'    DoCmd.RunCommand acCmdClose
'    DoCmd.RunSQL "INSERT INTO tbl1Employees"
'    DoCmd.Save
'    DoCmd.SendObject acSendReport, "Report1", acFormatPDF, "xipooo@gmail.com", , , "Test", "Test 1 2 3"
'    DoCmd.ShowToolbar "Ribbon", acToolbarNo
'    DoCmd.ShowToolbar "Ribbon", acToolbarYes
'    DoCmd.TransferDatabase acExport, , "Database1.accdb"
End Sub

Private Sub btnForward_Click()
    DoCmd.GoToRecord , , acNext
End Sub

Private Sub btnStop_Click()
    DoCmd.Hourglass False
End Sub

Private Sub FormFooter_Click()

End Sub
==========
                        
========== 41 VBA - CurrentProject ==========

========== 42 VBA - CurrentDB ==========

========== 43 VBA - SysCmd ==========

========== 44. VBA - Environ ==========





========== Puste Pole Błąd + otwieranie kwerendy ==========
Private Sub Polecenie5_Click()
    Dim Blad
    If IsNull(Lista2) Then
        Blad = MsgBox("Musisz wybrać przedmiot z listy!", vbOKOnly, "Błąd")
    Else
        DoCmd.OpenQuery "towary Kwerenda", , acReadOnly
    End If
End Sub
====================



========== Puste pole + sprawdzanie czy przedmiot znajduje się na drugiej liście + dodanie do listy i jej odświerzenie ==========
Private Sub Polecenie12_Click()
    Dim Blad
    If IsNull(Lista2) Then
        Blad = MsgBox("Musisz wybrać przedmiot z listy!", vbOKOnly, "Błąd")
    End If
    
    Dim i As Integer
    For i = 0 To Lista10.ListCount
        If (Lista10.Column(0, i) = CInt(Lista2.Value)) Then
            Blad = MsgBox("Masz to już w koszyku!", vbOKOnly, "Błąd")
            Exit Sub
        End If
    Next i

    Lista10.AddItem (Lista2.Column(0, Lista2.ListIndex) + ";" + Lista2.Column(1, Lista2.ListIndex))
    Lista10.Requery
End Sub
====================




========== Jeżeli w liście coś się znajduje to ją opróżnij ==========
Private Sub Polecenie36_Click()
    While Lista10.ListCount > 0
        Lista10.RemoveItem (0)
    Wend
End Sub
====================


                  
                  
                  
========== Łopatologicznie i z urzyciem tabeli koszyk - Puste pole + sprawdzanie czy przedmiot znajduje się na drugiej liście + dodanie do listy i jej odświerzenie ==========
Private Sub Polecenie12_Click()

    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim koszyk As Variant
                      
    Set db = CurrentDb
    Set rs = db.OpenRecordset("koszyk")
 
    If IsNull(Me![Lista2]) Then
          MsgBox "Zaznacz Produkt!"
          Exit Sub
    End If
 
    If [Lista2] = [Lista10] Then
          MsgBox "Produkt jest już w koszyku!"
          Exit Sub
    End If
 
    Dim Blad
    Dim i As Integer
    For i = 0 To Lista10.ListCount
            If (CInt(Lista2.Value) = Lista10.Column(0, i)) Then
                Blad = MsgBox("Masz juz to w koszyku!", vbOKOnly, "blad")
                Exit Sub
            End If
    Next i

    rs.AddNew
    rs!IdTowaru = Me.Lista2.Column(0)
    rs!Nazwa = Me.Lista2.Column(1)
    rs.Update
 
    rs.Close
    Set rs = Nothing
    Set db = Nothing

    Lista10.Requery
End Sub
====================

                                
                                
                                
========== Błąd nie wybrania z listy ==========
    Dim Blad
    If IsNull(Lista56) Then
        Blad = MsgBox("Musisz wybrać przedmiot z listy!", vbOKOnly, "Błąd")
    Else
        DoCmd.OpenForm "Produkty Formularz", , , "ProduktID =" & Me.Lista56.Value, acFormEdit
    End If
==========
                         
                                
                                
                                

                                
========== Logowanie i hasło ==========    
Option Compare Database
Option Explicit

Private Sub Polecenie4_Click()
    Dim rs As Recordset
    Dim db As Database

    Set rs = CurrentDb.OpenRecordset("Aptekarze", dbOpenSnapshot, dbReadOnly)
    
    rs.FindFirst "Login='" & Me.Tekst0 & "'"
    
    If rs.NoMatch = True Then
        Me.Etykieta5.Visible = True
        Me.Tekst0.SetFocus
        Exit Sub
    End If
    Me.Etykieta5.Visible = False
    
    If rs!Haslo <> Me.Tekst2 Or IsNull(Me.Tekst2) Then
        Me.Etykieta7.Visible = True
        Me.Tekst2.SetFocus
        Exit Sub
    End If
    Me.Etykieta7.Visible = False
    DoCmd.OpenForm "Apteka Formularz"
    DoCmd.Close acForm, Me.Name
End Sub

==========
                                      
                                      
                                      
                                      
                                      
==========  Szyfrowanie ==========
Nowy modył > Modules > Module1 np.

                                      
Option Compare Database
Option Explicit
Public Const Salt As Long = 54321234

Public Function Encrypt(strIn As String) As String
    Dim strChr As String
    Dim i As Integer
    
    For i = 1 To Len(strIn)
        strChr = strChr & CStr(Asc(Mid(strIn, i, 1)) Xor Salt)
    Next i
    Encrypt = strChr
End Function


                                    
                                    
==============================
View > Immediate Window >
?encrypt("Hasło")
5432117854321203543211855432137754321213

Wynik wpisać do kolumny hasła w tebeli z której pobieramy hasło
==========


                                      
                                      
                                      
                                      
========== Logowanie z szyfrowaniem ==========                                
Option Compare Database
Option Explicit

Private Sub Polecenie4_Click()
    Dim rs As Recordset
    Dim db As Database

    Set rs = CurrentDb.OpenRecordset("Aptekarze", dbOpenSnapshot, dbReadOnly)
    
    rs.FindFirst "Login='" & Me.Tekst0 & "'"
    
    If rs.NoMatch = True Then
        Me.Etykieta5.Visible = True
        Me.Etykieta7.Visible = False
        Me.Tekst0.SetFocus
        Exit Sub
    End If
    Me.Etykieta5.Visible = False

    If IsNull(Me.Tekst2) Then
        Me.Etykieta7.Visible = True
        Me.Tekst2.SetFocus
        Exit Sub
    End If
    Me.Etykieta7.Visible = False
    
    
    If rs!Haslo <> Encrypt(Me.Tekst2) Then
        Me.Etykieta7.Visible = True
        Me.Tekst2.SetFocus
        Exit Sub
    End If
    Me.Etykieta7.Visible = False
    
    DoCmd.OpenForm "Apteka Formularz"
    DoCmd.Close acForm, Me.Name
End Sub


==========
                                      
==========
Login
https://www.youtube.com/watch?v=356ylQn6kkA&list=PLYMOUCVo86jEeMMdaaq03jQ_t9nFV737s&index=56&ab_channel=ProgrammingMadeEZ

Szyfrowanie hasła:
https://www.youtube.com/watch?v=x4FAouRZ21s&list=PLYMOUCVo86jEeMMdaaq03jQ_t9nFV737s&index=60&ab_channel=ProgrammingMadeEZ
========== ==========

==========
