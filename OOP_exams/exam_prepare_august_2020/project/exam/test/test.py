from unittest import TestCase, main

from exam.project import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team('team')
        self.team2 = Team('second')

    def test_initialised(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        self.assertEqual('team', self.team.name)
        self.assertEqual({'dido': 33, 'ivan': 15}, self.team.members)

    def test_name_validation_raise_if_have_integers(self):
        with self.assertRaises(ValueError) as ex:
            self.team = Team('team123')
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        kwargs = {'dido': 33, 'ivan': 15}
        result = self.team.add_member(**kwargs)
        self.assertEqual(f'Successfully added: dido, ivan', result)
        kwargs2 = {'victor': 33}
        result_2 = self.team.add_member(**kwargs2)
        self.assertEqual({'dido': 33, 'ivan': 15, 'victor': 33}, self.team.members)
        self.assertEqual(f'Successfully added: victor', result_2)

    def test_to_add_member_if_already_was_added(self):
        kwargs = {'dido': 33, 'ivan': 15}
        self.team.add_member(**kwargs)
        kwargs2 = {'dido': 33}
        result = self.team.add_member(**kwargs2)
        self.assertEqual('Successfully added: ', result)
        self.assertEqual({'dido': 33, 'ivan': 15}, self.team.members)

    def test_remove_member(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        result = self.team.remove_member('dido')
        self.assertEqual("Member dido removed", result)
        self.assertEqual({'ivan': 15}, self.team.members)

    def test_try_to_remove_member_not_in_list(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        result = self.team.remove_member('victor')
        self.assertEqual("Member with name victor does not exist", result)
        self.assertEqual({'dido': 33, 'ivan': 15}, self.team.members)

    def test_gt_two_instance(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        self.team2.members = {'dido': 33, 'ivan': 15, 'victor': 40}
        result = self.team < self.team2
        self.assertTrue(result)
        result = self.team > self.team2
        self.assertFalse(result)

    def test_length_of_team(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        result = len(self.team)
        self.assertEqual(2, result)

    def test_repr_add(self):
        team2 = Team('second')
        self.team.members = {'dido': 33, 'ivan': 15}
        team2.members = {'kiro': 33, 'sirakov': 15, 'victor': 40}
        result = self.team + team2
        self.assertEqual('teamsecond', result.name)
        self.assertEqual({'kiro': 33, 'sirakov': 15, 'victor': 40, 'dido': 33, 'ivan': 15}, result.members)

    def test_add_if_members_are_with_same_name(self):
        team2 = Team('second')
        self.team.members = {'dido': 33, 'ivan': 15}
        team2.members = {'dido': 33, 'ivan': 15, 'victor': 40}
        result = self.team + team2
        self.assertEqual('teamsecond', result.name)
        self.assertEqual({'dido': 33, 'ivan': 15,'victor': 40}, result.members)

    def test_repr_str(self):
        self.team.members = {'dido': 33, 'ivan': 15}
        result = self.team.__str__()
        expected = """Team name: team
Member: dido - 33-years old
Member: ivan - 15-years old"""
        self.assertEqual(expected, result)

    if __name__ == '__main__':
        main()
