package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

var (
	SHOP_SERVICE_URL = os.Getenv("SHOP_SERVICE_URL")
)

func main() {
	if SHOP_SERVICE_URL == "" {
		SHOP_SERVICE_URL = "http://localhost:8002"
	}

	router := gin.Default()

	router.GET("/item/:item_id", getItem)
	router.GET("/", base)

	router.Run(":8001")
}

func getItem(c *gin.Context) {
	itemID := c.Param("item_id")

	fmt.Println("SHOP_SERVICE_URL: ", SHOP_SERVICE_URL)
	url := fmt.Sprintf("%s/shop/item/%s", SHOP_SERVICE_URL, itemID)

	resp, err := http.Get(url)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Error fetching item details"})
		fmt.Printf("Error fetching item details from URL: %s\n", url)
		return
	}

	defer resp.Body.Close()

	var itemData map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&itemData); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Error decoding JSON"})
		return
	}

	c.JSON(http.StatusOK, itemData)
}

func base(c *gin.Context) {
	content := map[string]string{
		"hello": "from frontend",
	}

	c.JSON(http.StatusOK, content)
}
