class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_votes(self, num_votes):
        self.votes += num_votes

    def get_percentage(self, total_votes):
        return (self.votes / total_votes) * 100 if total_votes > 0 else 0


class Elections:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def conduct_election(self):
        for candidate in self.candidates:
            votes = int(input(f"Enter the number of votes for {candidate.name}: "))
            candidate.add_votes(votes)
        total_votes = sum(candidate.votes for candidate in self.candidates)

        for candidate in self.candidates:
            percentage = candidate.get_percentage(total_votes)
            print(f"{candidate.name}: {candidate.votes} votes ({percentage:.2f}%)")

        winner = max(self.candidates, key=lambda x: x.votes, default=None)
        if winner:
            print(f"\n{winner.name} is the winner with {winner.votes} votes!")
        else:
            print("\nNo winner. It's a tie!")


def main():
    election = Elections()

    for i in range(5):
        name = input(f"Enter the name of candidate {i + 1}: ")
        candidate = Candidate(name)
        election.add_candidate(candidate)

    election.conduct_election()


if __name__ == "__main__":
    main()






