import sys
from pathlib import Path

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from db.engine import SessionLocal
from db.models import Journal

def categorize_keyphrases(keyphrases):
    unigrams = [k for k in keyphrases if len(k.split()) == 1]
    bigrams = [k for k in keyphrases if len(k.split()) == 2]
    trigrams = [k for k in keyphrases if len(k.split()) == 3]
    others = [k for k in keyphrases if len(k.split()) > 3]
    return unigrams, bigrams, trigrams, others

def main():
    session = SessionLocal()
    journals = session.query(Journal).all()

    total_unigrams = total_bigrams = total_trigrams = total_others = 0

    for journal in journals:
        if journal.keyphrases:
            unigrams, bigrams, trigrams, others = categorize_keyphrases(journal.keyphrases)
            total_unigrams += len(unigrams)
            total_bigrams += len(bigrams)
            total_trigrams += len(trigrams)
            total_others += len(others)

    print(" N-gram Summary Across All Journals:")
    print(f"  • Total Journals Checked: {len(journals)}")
    print(f"  • Total Unigrams: {total_unigrams}")
    print(f"  • Total Bigrams: {total_bigrams}")
    print(f"  • Total Trigrams: {total_trigrams}")
    print(f"  • Extra-long phrases (4+ words): {total_others}")

if __name__ == "__main__":
    main()
