import java.util.ArrayList;
import java.util.Arrays;
import static java.util.Collections.reverse;
import java.util.List;

/**
 * Algorien
 * @version 0.0.1
 * @see <a href="https://github.com/ilies-t/algorien">https://github.com/ilies-t/algorien</a>
 * @author ilies t <a href="https://github.com/ilies-t">https://github.com/ilies-t</a>
 * @licence Apache License 2.0
 */
public class Algorien {

	/**
	 * Method to create an list with split characters and add previous characters for each loop.
	 * @param a string to be split
	 * @return list
	 */
	private static List<String> splitIncr(final String a) {
		final List<String> arr = Arrays.asList(
			a.toLowerCase().split("")
		);
		final List<String> finalArray = new ArrayList<>();
		StringBuilder item = new StringBuilder();

		/*
		example with 'beach':
			will become -> ['b', 'be', 'bea', 'beac', 'beach',
							'h', 'hc', 'hca', 'hcae', 'hcaeb']
			also, to avoid space problem, add a condition
		 */
		for (int i = 0; i < 2; i++) {
			arr.forEach((character) -> {
				if( !( character.equals(" ") ) ) {
					item.append(character);
					finalArray.add( item.toString() );
				}
			});

			// reinitialize actual item to ""
			item.setLength(0);

			// and reverse "arr" list
			reverse(arr);
		}

		return finalArray;
	}

	/**
	 * Search similarity of a word by reference.
	 * @param word word to be compared
	 * @param reference reference word
	 * @return percentage
	 */
	public static double search(final String word, final String reference) {

		double pct;
		final List<List<String>> result = Arrays.asList(
			Algorien.splitIncr(word),
			Algorien.splitIncr(reference)
		);

		// so check if each char in word array is present in reference array
		pct = result.get(0).stream().filter( (character) ->
			result.get(1).contains(character))
		.count();

		pct /= result.get(1).size();

		return Math.round((pct * 100.0) * 100.0) / 100.0;

	}
}
