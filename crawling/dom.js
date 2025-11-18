const axios = require('axios');
const cheerio = require('cheerio');

async function main() {
  const resp = await axios.get(
      'https://swgs.kookmin.ac.kr/swgs/major/ai-application.do'
  );

  const $ = cheerio.load(resp.data);
  const elements = $('h5');

  elements.each((idx, el) => {
    console.log($(el).text());
  });
}

main();
