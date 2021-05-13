import React, { useState } from 'react';
import { getBooks } from '../api';

export default () => {
  const [books, setBooks] = useState(getBooks());
  const [searchIsActive, setSearchIsActive] = useState(false);
  const [searchString, setSearchString] = useState('');

  const search = () => {
    if (!searchString) {
      return;
    }

    setSearchIsActive(true);
    setBooks(getBooks(searchString));
  };

  const clear = () => {
    setSearchIsActive(false);
    setBooks(getBooks());
    setSearchString('');
  };

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
              <img src={book.avatar} class='card-img-top' />
              <div class='card-body'>
                <h5 class='card-title'>{book.title}</h5>
                <h6 class='card-subtitle mb-2 text-muted'>
                  {book.writer}, {book.year}
                </h6>
                <p class='card-text'>{book.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
