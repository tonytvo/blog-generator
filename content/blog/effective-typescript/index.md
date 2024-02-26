---
title: effective typescript summary
date: "2024-03-05T22:12:03.284Z"
description: "effective typescript summary"
tags: ["agiletechnicalpractices", "programming"]
---


# Avoid Cluttering Your Code with Inferable Types

- example 1:

Don’t write:

```javascript
let x: number = 12;
```

Instead, just write:

```javascript
let x = 12;
```

- example 2:

Instead of:

```javascript
const person: {
  name: string;
  born: {
    where: string;
    when: string;
  };
  died: {
    where: string;
    when: string;
  }
} = {
  name: 'Sojourner Truth',
  born: {
    where: 'Swartekill, NY',
    when: 'c.1797',
  },
  died: {
    where: 'Battle Creek, MI',
    when: 'Nov. 26, 1883'
  }
};
```
you can just write:

```javascript
const person = {
  name: 'Sojourner Truth',
  born: {
    where: 'Swartekill, NY',
    when: 'c.1797',
  },
  died: {
    where: 'Battle Creek, MI',
    when: 'Nov. 26, 1883'
  }
};
```

- example 3:

instead of:

```javascript
interface Product {
  id: number;
  name: string;
  price: number;
}

function logProduct(product: Product) {
  const id: number = product.id;
  const name: string = product.name;
  const price: number = product.price;
  console.log(id, name, price);
}
```

you can just write:

```javascript
interface Product {
  id: number;
  name: string;
  price: number;
}

function logProduct(product: Product) {
  const {id, name, price} = product;
  console.log(id, name, price);
}
```

- example 4:

```javascript
// Don't do this:
app.get('/health', (request: express.Request, response: express.Response) => {
  response.send('OK');
});
```

```javascript
// Do this:
app.get('/health', (request, response) => {
  response.send('OK');
});
```

- There are a few situations where you may still want to specify a type even where it can be inferred.

  - when you define an object literal
```javascript
const elmo: Product = {
  name: 'Tickle Me Elmo',
  id: '048188 627152',
  price: 28.99,
};
```
    - When you specify a type on a definition like this, you enable excess property checking. This can help catch errors, particularly for types with optional fields.
    - You also increase the odds that an error will be reported in the right place (type error where it's defined vs type error where it's used)

  - You may still want to annotate return type even when it can be inferred to ensure that implementation errors don't leak out into uses of the function.
    - Writing out the return type may also help you think more clearly about your function: you should know what its input and output types are before you implement it. While the implementation may shift around a bit, the function's contract (its type signature) generally should not. This is similar in spirit to test-driven development (TDD), in which you write the tests that exercise a function before you implement it. Writing the full type signature first helps get you the function you want, rather than the one the implementation makes expedient.

- If you are using a linter, the eslint rule no-inferrable-types (note the variant spelling) can help ensure that all your type annotations are really necessary.

# Don’t Repeat Type Information in Documentation

- example 1:

```javascript
/**
 * Returns a string with the foreground color.
 * Takes zero or one arguments. With no arguments, returns the
 * standard foreground color. With one argument, returns the foreground color
 * for a particular page.
 */
function getForegroundColor(page?: string) {
  return page === 'login' ? {r: 127, g: 127, b: 127} : {r: 0, g: 0, b: 0};
}
```

better declaration and comment might look like this:

```javascript
interface Color {
  r: number;
  g: number;
  b: number;
}

/** Get the foreground color for the application or a specific page. */
function getForegroundColor(page?: string): Color {
  // ...
}
```

- Example 2:

```javascript
/** Does not modify nums */
function sort(nums: number[]) { /* ... */ }
```

declare it readonly and let TypeScript enforce the contract

```javascript
function sort(nums: readonly number[]) { /* ... */ }
```

- Avoid repeating type information in comments and variable names. In the best case it is duplicative of type declarations, and in the worst it will lead to conflicting information.

- Consider including units in variable names if they aren't clear from the type (e.g., timeMs or temperatureC).




# Quotes


# References
- https://www.typescriptlang.org/docs/handbook/
- https://www.typescriptlang.org/play
- https://github.com/danvk/effective-typescript
- https://effectivetypescript.com/
- https://github.com/microsoft/TypeScript/wiki/Performance
- https://google.github.io/styleguide/tsguide.html
