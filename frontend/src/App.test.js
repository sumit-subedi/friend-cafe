import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});





// 
// 
// 
{/* <table class="table"> */}
{/* <thead class="thead-dark"> */}
  {/* <tr> */}
    {/* <th scope="col">Item</th> */}
    {/* <th scope="col">Qty</th> */}
    {/* <th scope="col">Table</th> */}
  {/* </tr> */}
{/* </thead> */}
{/* <tbody> */}
  {/* {% for val in t %} */}
{/* <tr> */}
  {/* <td>{{val.item}}</td> */}
  {/* <td>{{val.qty}}</td> */}
  {/* <td>{{val.table_no}}</td> */}
{/* </tr> */}
{/* {% endfor %} */}
  {/*  */}
{/* </tbody> */}
{/* </table> */}