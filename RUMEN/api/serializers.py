from rest_framework import serializers
from .models import ChessBoard


class ChessBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessBoard
        fields = ('id', 'code', 'host', 'board', 'personToMove')


class CreateBoardSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = ChessBoard
        fields = ('code', 'board', 'personToMove')
