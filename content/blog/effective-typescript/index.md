---
title: effective typescript summary
date: "2024-03-05T22:12:03.284Z"
description: "effective typescript summary"
tags: ["agiletechnicalpractices", "programming"]
---

# Understand the relationship between typescript and javascript

- If you're migrating an existing javascript codebase to typesript. It means that you don't have to rewrite any of your code in another language to start using TypeScript and get the benefits it provides.

- one of the goals of TypeScript's type system is to detect code that will throw an exception at runtime, without having to run your code. The type checker cannot always spot code that will throw exceptions, but it will try.

- type annotations tell TypeScript what your intent is, and this lets it spot places where your code's behavior does not match your intent.

- [typescript is superset of javascript](./ts-superset-js.png)

- Things to remember
  - TypeScript is a superset of JavaScript. In other words, all JavaScript programs are already TypeScript programs. TypeScript has some syntax of its own, so typeScript programs are not, in general, valid JavaScript programs.
  - TypeScript adds a type system that models JavaScript's runtime behavior and tries to spot code which will throw exceptions at runtime. But you shouldn't expect it to flag every exception. It is possible for code to pass the type checker but still throw at runtime.
  - While TypeScript's type system largely models JavaScript behavior, there are some constructs that JavaScript allows but TypeScript chooses to bar, such as calling functions with the wrong number of arguments. This is largely a matter of taste.

# know which TypeScript Options You're Using

- if you mean to allow null, you can fix the error by making your intent explicit:
```javascript
const x: number | null = null;
```

- **Things to Remember**
  - The TypeScript compiler includes several settings which affect core aspects of the language.
  - Configure TypeScript using tsconfig.json rather than command-line. options.
  - Turn on noImplicit Any unless you are transitioning a JavaScript project to TypeScript.
  - Use strictNullChecks to prevent "undefined is not an object”- style runtime errors.
  - Aim to enable strict to get the most thorough checking that TypeScript can offer.

# Understand Evolving any

- example 1:
```javascript
const result = [];  // Type is any[]
result.push('a');
result  // Type is string[]
result.push(1);
result  // Type is (string | number)[]
```

- Implicit any types do not evolve through function calls. The arrow function here trips up inference:

```javascript
function makeSquares(start: number, limit: number) {
  const out = [];
     // ~~~ Variable 'out' implicitly has type 'any[]' in some locations
  range(start, limit).forEach(i => {
    out.push(i * i);
  });
  return out;
      // ~~~ Variable 'out' implicitly has an 'any[]' type
}
```
  - In cases like this, you may want to consider using an array's map and filter methods to build arrays in a single statement and avoid iteration and evolving any entirely


- **Things to Remember**
  - While TypeScript types typically only refine, implicit any and any[] types are allowed to evolve. You should be able to recognize and understand this construct where it occurs.
  - For better error checking, consider providing an explicit type annotation instead of using evolving any.

# push null values to the perimeter of your types

- example 1:
  - avoid
```javascript
let min, max;
...
return [min, max];
```
  - better approach would be:
```javascript
let result: [number, number] | null = null;
...
return result;
```

- mix of null and non-null values can also lead to problems in classes. For example
```javascript
class UserPosts {
  user: UserInfo | null;
  posts: Post [] | null;

  constructor () {
    this.user = null;
    this.posts = null;
  }

  async init(userId: string) {
    return Promise.all([
      async () => this.user = await fetchUser(userId),
      async () => this.posts = await fetchPostsForUser(userId)
    ]);
  }
}
```
  - better design would wait until all the data used by the class is available
```javascript
class UserPosts {
  user: UserInfo;
  posts: Post [];

  constructor () {
    this.user = null;
    this.posts = null;
  }

  async init(userId: string) {
    const [user, posts] = Promise.all([
      async () => this.user = await fetchUser(userId),
      async () => this.posts = await fetchPostsForUser(userId)
    ]);
    return new UserPosts(user, posts);
  }
}
```

- don't be tempted to replace nullable properties with promises. This tends to lead to even more confusing code and forces all your methods to be async. Promises clarify the code that loads data but tend to have the opposite effect on the class that uses that data.)

- **Things to Remember**
  - Avoid designs in which one value being null or not null is implicitly related to another value being null or not null.
  - Push null values to the perimeter of your API by making larger objects either null or fully non-null. This will make code clearer both for human readers and for the type checker.
  - Consider creating a fully non-null class and constructing it when all values are available.
  - While strictNullChecks may flag many issues in your code, it's indispensable for surfacing the behavior of functions with respect to null values.


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
