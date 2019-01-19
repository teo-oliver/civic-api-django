from django.test import TestCase
from django.utils import timezone

from .models import Vote
from .serializers import VoteSerializer

class VoteSerializer(TestCase):

    def test_serialization(self):
        time = timezone.now()
        vote = Vote.objects.create(
            subject='More projects built in Django'
            ayes=100,
            nays=0,
            vote_taken=time,

        )
        serialized = VoteSerializer(vote).data
        assert vote.id == serialized['id']
        assert vote.subject == serialized['subject']
        assert vote.ayes == serialized['ayes']
        assert vote.nays == serialized['nays']