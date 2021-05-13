import faker from 'faker';
import axios from 'axios';

const API_URL = 'http://localhost:8001';

// // TODO Mock books, remove after we have the api
// const BOOKS = [
//   ...new Array(50).fill(null).map((val, index) => ({
//     title: faker.lorem.words(2),
//     writer: `${faker.name.firstName()} ${faker.name.lastName()}`,
//     year: Math.floor(Math.random() * (2021 - 1980 + 1) + 1980),
//     description: faker.lorem.sentences(5),
//     avatar: faker.image.image(),
//     id: index,
//   })),
// ];

export const getBooks = async (searchString = '') => {
  const { data } = await axios.get(
    `${API_URL}/api/books${searchString ? '?search=' + searchString : ''}`
  );

  return data;
};

export const login = async (username, password) => {
  try {
    // await axios.post(`${API_URL}/login`, {
    //   username,
    //   password,
    // });

    return true;
  } catch (err) {
    return false;
  }
};
