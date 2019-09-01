	'Sub Ticker () calls on MinMax ()
	'only run sub Ticker ()
Sub Ticker():

    For Each Worksheet In Worksheets
    If ActiveSheet.Index = Worksheets.Count Then
        Worksheets(1).Select
        Else
        ActiveSheet.Next.Select
        End If
    Dim ws As Worksheet
    Set ws = ActiveSheet
            lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
            LastColumn = ws.Cells(1, Columns.Count).End(xlToLeft).Column
            Dim stock As String
            Dim StockVolume As Double
            StockVolume = 0
            Dim Summary_Table_row As Integer
            Dim OpenPrice As Double
            Dim ClosePrice As Double
            Dim MaxChange As Double
            Dim MinChange As Double
            Dim MaxVol As Double
            
            
            MaxChange = 0
            MinChange = 0
            MaxVol = 0
                                   
               
            Summary_Table_row = 2
            Cells(1, 9).Value = "Stock"
            Cells(1, 10).Value = "Yearly Change"
            Cells(1, 11).Value = "Percent Change"
            Cells(1, 12).Value = "Volume"
            Cells(2, 14).Value = "Greatest% Increase"
            Cells(3, 14).Value = "Greatest% Decrease"
            Cells(4, 14).Value = "Greatest Total Volume"
                     
            OpenPrice = Cells(2, 3).Value
        
            For i = 2 To lastRow
             On Error Resume Next
                    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                        stock = Cells(i, 1).Value
                        ClosePrice = Cells(i, 6).Value
                        StockVolume = StockVolume + Cells(i, 7).Value
                        Range("I" & Summary_Table_row).Value = stock
                        Range("J" & Summary_Table_row).Value = ClosePrice - OpenPrice
                        Range("K" & Summary_Table_row).Value = (ClosePrice - OpenPrice) / OpenPrice
                        Range("L" & Summary_Table_row).Value = StockVolume
                        OpenPrice = Cells(i + 1, 3).Value
                        Summary_Table_row = Summary_Table_row + 1
                        StockVolume = 0
                        Else
                        StockVolume = StockVolume + Cells(i, 7).Value
                End If
            Next i
        Call MinMax
        Cells.EntireColumn.AutoFit
                   
    Next
End Sub

Sub MinMax():
    Dim ws As Worksheet
    Set ws = ActiveSheet
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    Dim MaxChange As Double
    Dim MinChange As Double
    Dim MaxVol As Double
        For i = 2 To lastRow
            If Cells(i, 12).Value = "" Then
            Exit Sub
            Else
                If Cells(i, 10).Value < 0 Then
                Cells(i, 10).Interior.ColorIndex = 3
                Else
                Cells(i, 10).Interior.ColorIndex = 4
                End If
                      
                If Cells(i, 11).Value > MaxChange Then
                MaxChange = Cells(i, 11).Value
                Cells(2, 15).Value = Cells(i, 9).Value
                End If
                
                                                             
                Cells(2, 16).Value = MaxChange
                Cells(2, 16).NumberFormat = "0.00%"
                                
                If MinChange > Cells(i, 11).Value Then
                MinChange = Cells(i, 11).Value
                Cells(3, 15).Value = Cells(i, 9).Value
                End If
                
                Cells(3, 16).Value = MinChange
                Cells(3, 16).NumberFormat = "0.00%"
                
                If Cells(i, 12).Value > MaxVol Then
                MaxVol = Cells(i, 12).Value
                Cells(4, 15).Value = Cells(i, 9).Value
                End If
                                             
                Cells(4, 16).Value = MaxVol
                Cells(i, 11).NumberFormat = "0.00%"
            End If
         Next i
End Sub









