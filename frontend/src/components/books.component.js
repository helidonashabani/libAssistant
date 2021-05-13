import React, { useEffect, useState } from 'react';
import { getBooks } from '../api';

export default () => {
  const [books, setBooks] = useState([]);
  const [searchIsActive, setSearchIsActive] = useState(false);
  const [searchString, setSearchString] = useState('');

  const search = async () => {
    if (!searchString) {
      return;
    }

    setSearchIsActive(true);
    setBooks(await getBooks(searchString));
  };

  const clear = async () => {
    setSearchIsActive(false);
    setBooks(await getBooks());
    setSearchString('');
  };

  useEffect(() => {
    (async () => {
      const initBooks = await getBooks();
      setBooks(initBooks);
    })();
  }, []);

  return (
    <div className='content-wrapper'>
      <div className='content-inner'>
        <div>
          <h3>Books</h3>
        </div>
        <div>
          <div class='row g-3'>
            <div class='col-auto'>
              <input
                value={searchString}
                type='text'
                class='form-control'
                id='search'
                placeholder='Search...'
                onChange={(e) => setSearchString(e.target.value)}
              />
            </div>
            <div class='col-auto'>
              <button onClick={search} class='btn btn-primary mb-3'>
                Search
              </button>
            </div>
            {searchIsActive && (
              <div class='col-auto'>
                <button onClick={clear} class='btn btn-primary mb-3'>
                  Clear
                </button>
              </div>
            )}
          </div>
        </div>
        <div class='books-container'>
          {books.map((book) => (
            <div key={book.id} class='card'>
              <img src={book.image} class='card-img-top' />
              <div class='card-body'>
                <h5 class='card-title'>{book.title}</h5>
                <h6 class='card-subtitle mb-2 text-muted'>
                  {book.auth}, {book.publisher}
                </h6>
                <p class='card-text'>ISBN: {book.isbn}</p>
              </div>
            </div>
          ))}
          {searchIsActive && !books.length && 'No results.'}
        </div>
      </div>
    </div>
  );
};
