package ai.openobserve.product;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class ProductApplication {

	private static final String REVIEW_SERVICE_URL = System.getenv().getOrDefault("REVIEW_SERVICE_URL",
			"http://localhost:8004");

	public static void main(String[] args) {
		SpringApplication.run(ProductApplication.class, args);
	}

	@RestController
	public class ProductController {

		@GetMapping("/product/{productId}")
		public Map<String, Object> getProduct(@PathVariable int productId) {
			System.out.println("REVIEW_SERVICE_URL: " + REVIEW_SERVICE_URL);

			HashMap<String, Object> sampleProduct = new HashMap<>();
			sampleProduct.put("id", productId);
			sampleProduct.put("name", "Sample Product");
			sampleProduct.put("description", "This is a sample product.");

			try {
				RestTemplate restTemplate = new RestTemplate();
				Map reviewData = restTemplate.getForObject(REVIEW_SERVICE_URL + "/review/" + productId, Map.class);

				sampleProduct.put("review", reviewData.get("review"));
				sampleProduct.put("rating", reviewData.get("rating"));

			} catch (HttpClientErrorException e) {
				throw new RuntimeException("Error fetching review", e);
			}

			return sampleProduct;
		}

		@GetMapping("/")
		public Map<String, String> base() {
			HashMap<String, String> content = new HashMap<>();
			content.put("hello", "from product");
			return content;
		}
	}
}
