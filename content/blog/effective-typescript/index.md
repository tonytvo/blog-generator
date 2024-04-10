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

# understand that code generation is independent of types

- At a high level, tsc (the TypeScript compiler) does two things:
  - It converts next-generation TypeScript/JavaScript to an older version of JavaScript that works in browsers ("transpiling").
  - It checks your code for type errors.
- The types in your code cannot affect the JavaScript that TypeScript emits. Since it's this JavaScript that gets executed, this means that your types can't affect the way your code runs.
- Code with Type Errors Can Produce Output because Because code output is independent of type checking

```bash
$ cat test.ts
let x 'hello';
X = 1234;
$ tsc test.ts
test.ts:2:1- error TS2322: Type '1234' is not assignable to type 'string'
2 x = 1234;

$ cat test.js
var x = 'hello';
x = 1234;
```

- You can think of all TypeScript errors as being similar to warnings in those languages: it's likely that they indicate a problem and are worth investigating, but they won't stop the build.
  - It's better to say that your code has errors, or that it "doesn't type check."

- You should aim for zero errors when you commit code, lest you fall into the trap of having to remember what is an expected or unexpected error. If you want to disable output on errors, you can use the noEmitOnError option in tsconfig.json, or the equivalent in your build tool.

- **You Cannot Check TypeScript Types at Runtime**


- **Things to Remember**
  - Code generation is independent of the type system. This means that TypeScript types cannot affect the runtime behavior or performance of your code.
    - the TypeScript compiler will introduce build time overhead. The TypeScript team takes compiler performance seriously and compilation is usually quite fast, especially for incremental builds. If the overhead becomes significant, your build tool may have a "transpile only" option to skip the type checking.
    - The code that TypeScript emits to support older runtimes may incur a performance overhead vs. native implementations. For example, if you use generator functions and target ES5, which predates generators, then tsc will emit some helper code to make things work. This may have some overhead vs. a native implementation of generators. In any case, this has to do with the emit target and language levels and is still independent of the types.
```javascript
function as Number (val: number | string): number {
  return val as number;
}
// Looking at the generated JavaScript makes it clear what this function really does:
function as Number (val) {
  return val;
}

//There is no conversion going on whatsoever. The as number is a type operation, so it cannot affect the runtime behavior of your code. To normalize the value you'll need to check its runtime type and do the conversion using JavaScript constructs:
function asNumber (val: number | string): number {
  return typeof(val) === 'string' ? Number(val): val;
}
```

  - **runtime types may not be the same as declared types**
```javascript
function setLightSwitch (value: boolean) { 
  switch (value) {
    case true:
      turnLighton();
      break;
    case false:
      turnLightOff();
      break;
    default:
    console.log("Im afraid I cant do that.");
  }
}
// The key is to remember that boolean is the declared type. Because it is a TypeScript type, it goes away at runtime. In JavaScript code, a user might inadvertently call setLightSwitch with a value like "ON"
```

  - **You Cannot Overload a Function Based on TypeScript Types** 
    - Languages like C++ allow you to define multiple versions of a function that differ only in the types of their parameters. This is called "function overloading" Because the runtime behavior of your code is independent of its TypeScript types, this construct isn't possible in TypeScript:

```javascript
function add(a: number, b: number) { return a + b; } // Duplicate function implementation 
function add(a: string, b: string) { return a + b; } // Duplicate function implementation

// TypeScript does provide a facility for overloading functions, but it operates entirely at the type level. You can provide multiple declarations for a function, but only a single implementation:
function add (a: number, b: number): number;
function add (a: string, b: string): string;
function add (a, b) {
  return a + b;
}
const three add(1, 2); // Type is number
const twelve = add('1', '2'); // Type is string
//The first two declarations of add only provide type information. When TypeScript produces JavaScript output, they are removed, and only the implementation remains. 
```

  - It is possible for a program with type errors to produce code ("compile").
  - TypeScript types are not available at runtime. To query a type at runtime, you need some way to reconstruct it. Tagged unions and property checking are common ways to do this. Some constructs, such as class, introduce both a TypeScript type and a value that is available at runtime.
```javascript
//check for property example
function calculate Area (shape: Shape) {
if ('height' in shape) {
shape; // Type is Rectangle
return shape.width * shape.height;
} else {
shape; // Type is Square

// tagged unions example
interface Square {
  kind: 'square';
  width: number;
}
interface Rectangle {
  kind: 'rectangle';
  height: number;
  width: number;
}
type Shape = Square | Rectangle;

// class constructs introduce both a type and a value
class Square {
  constructor (public width: number) {}
}
class Rectangle extends Square {
  constructor (public width: number, public height: number) { super(width); }
}
type Shape = Square | Rectangle;
function calculateArea (shape: Shape) {
  if (shape instanceof Rectangle) {
    shape; // Type is Rectangle 
    return shape.width * shape.height;
  } else {
    shape;// Type is Square return shape.width
    return shape.width*shape.width; // OK
  }
}
//this works because class Rectangle introduces both a type and a value, whereas interface only introduced a type
//The Rectangle in type Shape = Square | Rectangle refers to the type, but the Rectangle in shape instanceof Rectangle refers to the value.
```

# get comfortable with structural typing javascript

- javascript is inherently duck typed: if you pass a function a value with all the right properties, it won't care how you made the value. It will just use it. ("If it walks like a duck and talks like a duck...")

- Understand that JavaScript is duck typed and TypeScript uses structural typing to model this: values assignable to your interfaces might have properties beyond those explicitly listed in your type declarations. Types are open and are not "sealed."


```javascript
// Say you're working on a physics library and have a 2D vector type:
interface Vector2D {
  x: number;
  y: number;
}

//You write a function to calculate its length:
function calculateLength(v: Vector2D) { return Math.sqrt(v.x * v.x + v.y * v.y); }

// now you introduce the notion of a named vector
interface NamedVector { name: string;
  x: number;
  y: number;
}

//The calculateLength function will work with NamedVectors because they have x and y properties, which are numbers. TypeScript is smart enough to figure this out
const v NamedVector = {x: 3, y: 4, name: 'Zee' }; 
calculateLength (v); // OK, result is 5

//What is interesting is that you never declared the relationship between Vector2D and NamedVector. 
//And you did not have to write an alternative implementation of calculateLength for NamedVectors.
//It allowed calculateLength to be called with a NamedVector because its structure was compatible with Vector2D

// this can also lead to trouble with 3D vector type as  the calculateLength only use x, y (and ignore z) to calculate the length
interface Vector3D {
  x: number;
  y: number;
  z: number;
}


function calculateLengthL1 (v: Vector3D) { 
  let length = 0;
  for (const axis of Object.keys(v)) { 
    const coord = v[axis]; // Element implicitly has an 'any' type because
                           // 'string' can't be used to index type 'Vector3D'
    length + Math.abs (coord);
  }
  return length;
}
// this logic assumes that Vector3D is sealed and does not have other properties, but it could
const vec3D = {x: 3, y: 4, z: 1, address: '123 Broadway');
calculateLengthL1 (vec3D); // OK, returns NaN

//but in this case an implementation without loops would be better:
function calculate LengthL1 (v: Vector3D) { return Math.abs (v.x) + Math.abs (v. y) + Math.abs (v.z); }

// Structural typing can also lead to surprises with classes, which are compared structurally for assignability:
// Be aware that classes also follow structural typing rules. You may not have an instance of the class you expect!
class C { 
  foo: string; 
  constructor (foo: string) { this.foo = foo; }
}
const c = new C('instance of C'); 
const d: C = { foo: 'object literal' }; // OK!

// Structural typing is beneficial when you're writing tests.
// Say you have a function that runs a query on a database and processes the results:
interface Author {
  first: string;
  last: string;
}
function getAuthors (database: PostgresDB): Author[] {
  const authorRows = database.runQuery(`SELECT FIRST, LAST FROM AUTHORS`);
  return authorRows.map(row => ({first: row[0], last: row[1]}));
}

// To test this, you could create a mock PostgresDB. But a better approach is to use structural typing and define a narrower interface:
interface DB {
  runQuery: (sql: string) => any [];
}

function getAuthors (database: DB): Author[] { 
  const authorRows = database.runQuery(`SELECT FIRST, LAST FROM AUTHORS`);
  return authorRows.map(row => ({first: row[0], last: row[1]}));
}

//You can still pass getAuthors a PostgresDB in production since it has a runQuery method.
//Because of structural typing, the PostgresDB doesn't need to say that it implements DB.
test('getAuthors', () => {
  const authors = getAuthors ({ 
    runQuery(sql: string) {
      return [['Toni', 'Morrison'], ['Maya', 'Angelou']];
    }
  });

  expect (authors).toEqual([
    {first: 'Toni', last: 'Morrison'},
    {first: 'Maya', last: 'Angelou'}
  ]);
});

// TypeScript will verify that our test DB conforms to the interface. 
// And your tests don't need to know anything about your production database: no mocking libraries necessary!
// By introducing an abstraction (DB), we've freed our logic (and tests) from the details of a specific implementation (PostgresDB).
// Another advantage of structural typing is that it can cleanly sever dependencies between libraries.
```

# limit use of the any Type


TypeScript's type system is gradual and optional: gradual because you can add types to your code bit by bit and optional because you can disable the type checker whenever you like. The key to these features is the any type:
//
let age: number;
age = '12';
NNN
Type "12" is not assignable to type 'number'
age = '12' as any; // OK
The type checker is right to complain here, but you can silence it just by typing as any. As you start using TypeScript, it's tempting to use any types and type assertions (as any) when you don't understand an error, think the type checker is incorrect, or simply don't want to take the time to write out type declarations. In some cases this may be OK, but be aware that any


eliminates many of the advantages of using TypeScript. You should at least understand its dangers before you use it.
There's No Type Safety with any Types
In the preceding example, the type declaration says that age is a number. But any lets you assign a string to it. The type checker will believe that it's a number (that's what you said, after all), and the chaos will go uncaught:
age += 1; // OK; at runtime, age is now "121"
any Lets You Break Contracts
When you write a function, you are specifying a contract: if the caller gives you a certain type of input, you'll produce a certain type of output. But with an any type you can break these contracts:
function calculateAge (birthDate: Date): number { // ...
}
let birthDate: any = '1990-01-19'; calculateAge (birthDate); // OK
The birth date parameter should be a Date, not a string. The any type has let you break the contract of calculateAge. This can be particularly problematic because JavaScript is often willing to implicitly convert between types. A string will sometimes work where a number is expected, only to
break in other circumstances.
There Are No Language Services for any Types
When a symbol has a type, the TypeScript language services are able to provide intelligent autocomplete and contextual documentation (as shown in Figure 1-3).
let person= person.
{ first: 'George', last: 'Washington' };
first last
Figure 1-3. The TypeScript Language Service is able to provide contextual autocomplete for symbols with types.
but for symbols with an any type, you're on your own (Figure 1-4). let person: any first: 'George', last: 'Washington' }; person.
Figure 1-4. There is no autocomplete for properties on symbols with any types. Renaming is another such service. If you have a Person type and functions to format a person's name:
interface Person { first: string; last: string;


}
const formatName = (p: Person) => `${p.first} ${p.last}`; const formatNameAny = (p: any) => `${p.first} ${p.last}`;
then you can select first in your editor, choose "Rename Symbol," and change it to firstName (see Figures 1-5 and 1-6).
interface Person {
}
first string
li Go to Definition
Go to Type Definition
F12
XF12
interface Person {
}
first: string;
firstName
Figure 1-6. Choosing the new name. The TypeScript language service ensures that all uses of the symbol in the project are also renamed. This changes the formatName function but not the any version:
F12
}
Peek Definition
Find All References
Peek References
Rename Symbol
F2
Figure 1-5. Renaming a symbol in vscode.
F12
interface Person {
firstName: string;
last: string;
const formatName = (p: Person) =>
${p.firstName} ${p.last}`; const formatNameAny (p: any) => `${p.first} ${p.last}`;
TypeScript's motto is "JavaScript that scales." A key part of "scales" is the language services, which are a core part of the TypeScript experience (see Item 6). Losing them will lead to a loss in productivity, not just for you but for everyone else working with your code.
any Types Mask Bugs When You Refactor Code
Suppose you're building a web application in which users can select some sort of item. One of your components might have an onSelectItem



callback. Writing a type for an Item seems like a hassle, so you just use any as
a stand-in:
interface Component Props {
}
onSelectItem: (item: any) => void;
Here's code that manages that component:
function render Selector(props: ComponentProps) { /*
. */ }
let selectedId: number = 0;
function handleSelectItem(item: any) {
selectedId= item. id;
}
renderSelector({onSelectItem: handleSelectItem});
Later you rework the selector in a way that makes it harder to pass the whole item object through to onSelectItem. But that's no big deal since you just need the ID. You change the signature in Component Props:
interface Component Props {
}
onSelectItem: (id: number) => void;
You update the component and everything passes the type checker. Victory! ...or is it? handleSelectItem takes an any parameter, so it's just as happy with an Item as it is with an ID. It produces a runtime exception, despite
passing the type checker. Had you used a more specific type, this would have been caught by the type checker.
any Hides Your Type Design
The type definition for complex objects like your application state can get quite long. Rather than writing out types for the dozens of properties in your page's state, you may be tempted to just use an any type and be done with it. This is problematic for all the reasons listed in this item. But it's also problematic because it hides the design of your state. As Chapter 4 explains, good type design is essential for writing clean, correct, and understandable code. With an any type, your type design is implicit. This makes it hard to know whether the design is a good one, or even what the design is at all. If you ask a coworker to review a change, they'll have to reconstruct whether and how you changed the application state. Better to write it out for everyone to see.
any Undermines Confidence in the Type System
Every time you make a mistake and the type checker catches it, it boosts your confidence in the type system. But when you see a type error at runtime, that confidence takes a hit. If you're introducing TypeScript on a larger team, this might make your coworkers question whether TypeScript is worth the effort. any types are often the source of these uncaught errors.


TypeScript aims to make your life easier, but TypeScript with lots of any types can be harder to work with than untyped JavaScript because you have to fix type errors and still keep track of the real types in your head. When your types match reality, it frees you from the burden of having to keep type information in your head. TypeScript will keep track of it for you.
For the times when you must use any, there are better and worse ways to do it. For much more on how to limit the downsides of any, see Chapter 5.
Things to Remember
• The any type effectively silences the type checker and TypeScript language services. It can mask real problems, harm developer experience, and undermine confidence in the type system. Avoid using it when you can!


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
