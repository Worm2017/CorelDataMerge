// Դ��ֻ��Ϊ�˷��㿴��ʵ�ʱ༭��  sRGB.cz.cc.gms

VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UniteOne 
   Caption         =   "CorelDRAW �ϲ���ҳΪһҳ By �m���� 2010"
   ClientHeight    =   4005
   ClientLeft      =   45
   ClientTop       =   330
   ClientWidth     =   5220
   OleObjectBlob   =   "UniteOne.frx":0000
   StartUpPosition =   1  '����������
End
Attribute VB_Name = "UniteOne"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Declare Function ShellExecute Lib "shell32.dll" Alias "ShellExecuteA" (ByVal hwnd As Long, ByVal lpOperation As String, ByVal lpFile As String, ByVal lpParameters As String, ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
Private Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Long

Option Explicit


 Dim iHang, iLie, iPages As Integer     '��������(Y) ����(X)
 Dim iYouyi, iXiayi As Single   '����(R) ����(B)
                                'txtHang, txtLie, txtYouyi, txtXiayi ,txtInfo
 Dim LogoFile As String         'Logo
 
 Dim s(1 To 255) As Shape   '����������ڴ��ÿҳ��Ⱥ��
 Dim p As Page          '�����ҳ
 

'**** ������  ִ��
Private Sub cmdRun_Click()

 Dim x_M, y_M
 ActiveDocument.Unit = cdrMillimeter
 ActiveDocument.EditAcrossLayers = False    '��ͼ��༭��ֹ
 
 For Each p In ActiveDocument.Pages
    p.Activate                    '����ÿҳ
    p.Shapes.All.CreateSelection          'ÿҳȫѡ
    Set s(p.Index) = ActiveSelection.Group    '���ÿҳ��Ⱥ��
 Next p
 
 ActiveDocument.EditAcrossLayers = True     '��ͼ��༭����
 
  x_M = y_M = 0
  
  For Each p In ActiveDocument.Pages
    p.Activate
       
    s(p.Index).MoveToLayer ActivePage.DesktopLayer    'ÿҳ�����ƶ��������
    s(p.Index).Move (iYouyi * x_M), -(300 + iXiayi * y_M) '���ж���  ��ƫ�ƣ���ƫ��
  
  y_M = y_M + 1
  
  If y_M = iLie Then
  x_M = x_M + 1
  y_M = 0
  End If
  
 Next p
 
 


 Unload Me 'ִ����ɹر�

End Sub



Private Sub Label6_Click()

End Sub

Private Sub Label9_Click()

End Sub

'*********** ��ʼ������ ***************
Private Sub UserForm_Initialize()

 Dim s As Shape
ActiveDocument.Unit = cdrMillimeter '���ĵ���λΪmm

 For Each p In ActiveDocument.Pages
 iPages = p.Index
 If iPages = 1 Then
  p.Activate
  p.Shapes.All.CreateSelection

 Set s = ActiveDocument.Selection
        If s.Shapes.Count = 0 Then
            MsgBox "��ǰ�ļ���һҳ�հ�û�������"
            Exit Sub
        End If
 
 End If
 Next p
 

 txtLie.Text = 5
 txtHang.Text = Int(iPages / CInt(txtLie.Text) + 0.9)
 txtLie.Text = Int(iPages / CInt(txtHang.Text) + 0.9)
 
 iHang = CInt(txtHang.Text)
 iLie = CInt(txtLie.Text)
 
 
 iYouyi = Int(s.SizeWidth + 0.6)
 iXiayi = Int(s.SizeHeight + 0.6)
 
 txtYouyi.Text = iYouyi
 txtXiayi.Text = iXiayi
 
 
 
  LogoFile = Path & "GMS\sRGB.cz.cc"
  

 txtInfo.Text = "���ĵ��� " & iPages & " ҳ����ҳ����ߴ�(mm):" & s.SizeWidth & "��" & s.SizeHeight
  
End Sub



'����

Private Sub cmdHelp_Click()

WebHelp

txtInfo.Text = "������� Http://sRGB.cz.cc ��ϸ����,Ѱ�Ҹ������Ƶ�̳̣�"
txtInfo.ForeColor = &HFF0000
cmdHelp.Caption = "���߰���"
cmdHelp.ForeColor = &HFF0000


End Sub


Private Sub LogoPic_MouseDown(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)
  
  If ExistsFile_UseFso(LogoFile) Then
    LogoPic.Picture = LoadPicture(LogoFile)   '��LOGOͼ
  End If
  
txtInfo.Text = "��������Ůѽ����֪������QQ���𣿻�ӭ���� Http://sRGB.cz.cc "
 
UniteOne.Repaint
End Sub

Private Sub txtInfo_MouseDown(ByVal Button As Integer, ByVal Shift As Integer, ByVal X As Single, ByVal Y As Single)

 WebHelp

End Sub

'�ر�
Private Sub cmdClose_Click()
Unload Me
End Sub


'VB�����ı���ֻ���������ֺ�С����
Private Sub txtHang_KeyPress(ByVal KeyAscii As MSForms.ReturnInteger)
Dim Numbers As String
Numbers = "1234567890"
If InStr(Numbers, Chr(KeyAscii)) = 0 Then
KeyAscii = 0
End If
End Sub

Private Sub txtLie_KeyPress(ByVal KeyAscii As MSForms.ReturnInteger)
Dim Numbers As String
Numbers = "1234567890"
If InStr(Numbers, Chr(KeyAscii)) = 0 Then
KeyAscii = 0
End If
End Sub

Private Sub txtXiayi_KeyPress(ByVal KeyAscii As MSForms.ReturnInteger)
Dim Numbers As String
Numbers = "1234567890" + Chr(8) + Chr(46)
If InStr(Numbers, Chr(KeyAscii)) = 0 Then
KeyAscii = 0
End If
End Sub

Private Sub txtYouyi_KeyPress(ByVal KeyAscii As MSForms.ReturnInteger)
Dim Numbers As String
Numbers = "1234567890" + Chr(8) + Chr(46)
If InStr(Numbers, Chr(KeyAscii)) = 0 Then
KeyAscii = 0
End If
End Sub

Private Sub txtHang_Change()
    Dim n As Single
    n = Val(txtHang.Text)
    If n > 0 And n < 1001 Then
        HangSpin.Value = n
        iHang = n
    End If
 
 txtHang.Text = iHang
 txtLie.Text = Int(iPages / iHang + 0.9)
 
  
  iLie = CInt(txtLie.Text)
    
End Sub

Private Sub HangSpin_Change()
    txtHang.Text = CStr(HangSpin.Value)
End Sub

Private Sub txtLie_Change()
    Dim n As Single
    n = Val(txtLie.Text)
    If n > 0 And n < 1001 Then
        LieSpin.Value = n
        iLie = n
    End If
    
    txtLie.Text = iLie
    txtHang.Text = Int(iPages / iLie + 0.9)
    
    iHang = CInt(txtHang.Text)
End Sub

Private Sub LieSpin_Change()
    txtLie.Text = CStr(LieSpin.Value)
End Sub


Private Sub txtXiayi_Change()
    Dim n As Single
    n = Val(txtXiayi.Text)
    If n > 0 And n < 1001 Then
        iXiayi = n
    End If
End Sub

Private Sub txtYouyi_Change()
    Dim n As Single
    n = Val(txtYouyi.Text)
    If n > 0 And n < 1001 Then
        iYouyi = n
    End If
End Sub






' ************* ����ģ�� ************* '
Function ExistsFile_UseFso(strPath As String) As Boolean

     Dim fso

     Set fso = CreateObject("Scripting.FileSystemObject")

     ExistsFile_UseFso = fso.FileExists(strPath)

     Set fso = Nothing

End Function

Function WebHelp()
 Dim h As Long, r As Long
 
 If cmdHelp.Caption = "���߰���" Then
 h = FindWindow(vbNullString, "CorelDRAW �ϲ���ҳΪһҳ By �m���� 2010")
 r = ShellExecute(h, "", "http://sRGB.cz.cc", "", "", 1)
 End If
End Function


Private Sub ƫ����ѡ��_Click()

End Sub
