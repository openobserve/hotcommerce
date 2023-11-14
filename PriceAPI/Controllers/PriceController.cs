using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace PriceAPI.Controllers
{
  [ApiController]
  [Route("[controller]")]
  public class PriceController : ControllerBase
  {
    [HttpGet]
    public ActionResult<string> Get()
    {
      return "Welcome to PriceAPI!";
    }

    [HttpGet("{id}")]
    public IActionResult GetPrice(int id)
    {
      var price = new PriceStructure
      {
        Id = id,
        Price = 100.0m
      };

      return Ok(price);
    }

    public class PriceStructure
    {
      public int Id { get; set; }
      public decimal Price { get; set; }
    }
  }
}

