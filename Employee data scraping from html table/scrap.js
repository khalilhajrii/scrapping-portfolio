const axios = require("axios");
const cheerio = require("cheerio");
const ObjectsToCsv = require("objects-to-csv");
const json2xls = require('json2xls');
const fs = require('fs');


(async function html_scraper() {
    employeeData = [];
    heading=[];
    CsvString = "";
    const response = await axios('https://datatables.net/examples/styling/display.html');
    console.log(response.status)
    const html = await response.data;
    const $ = cheerio.load(html);
    const allRows = $('table.display > tbody > tr');
    allRows.each((index, element) => {
        const tds = $(element).find('td');
        const name = $(tds[0]).text();
        const position = $(tds[1]).text();
        const office = $(tds[2]).text();
        const age = $(tds[3]).text();
        const startDate = $(tds[4]).text();
        const salary = $(tds[5]).text();

        employeeData.push({
            'Name': name,
            'Position': position,
            'Office': office,
            'Age': age,
            'Start Date': startDate,
            'Salary': salary,
        })
    })
    const xls = json2xls(employeeData);
    fs.writeFileSync('C:\projects\Scrapping\scrapped.xlsx', xls, 'binary');
})();