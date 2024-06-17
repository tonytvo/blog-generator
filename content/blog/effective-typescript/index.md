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

- The "any type" effectively silences the type checker and TypeScript language services. It can mask real problems, harm developer experience, and undermine confidence in the type system. Avoid using it when you can!

- TypeScript's type system is *gradual and optional*: *gradual* because you can add types to your code bit by bit and *optional* because you can disable the type checker whenever you like. The key to these features is the any type:

```javascript
let age: number;
age = '12'; // Type "12" is not assignable to type 'number'
age = '12' as any; // OK
//The type checker is right to complain here, but you can silence it just by typing as any.
```

- **There's No Type Safety with any Types**
  - In the preceding example, the type declaration says that age is a number. But any lets you assign a string to it. The type checker will believe that it's a number (that's what you said, after all), and the chaos will go uncaught:

```javascript
age += 1; // OK; at runtime, age is now "121"
```

- **any Lets You Break Contracts**

  - When you write a function, you are specifying a contract: if the caller gives you a certain type of input, you'll produce a certain type of output. But with an any type you can break these contracts:

```javascript
function calculateAge (birthDate: Date): number { // ... 
}
let birthDate: any = '1990-01-19'; calculateAge (birthDate); // OK
```

- **There Are No Language Services for any Types**
  - When a symbol has a type, the TypeScript language services are able to provide intelligent autocomplete and contextual documentation  but for symbols with an any type, you're on your own

  - Renaming is another such service. If you have a Person type and functions to format a person's name:

```javascript
interface Person { first: string; last: string; }
const formatName = (p: Person) => `${p.first} ${p.last}`; const formatNameAny = (p: any) => `${p.first} ${p.last}`;
```

  - TypeScript's motto is "JavaScript that scales." A key part of "scales" is the language services, which are a core part of the TypeScript experience. Losing them will lead to a loss in productivity, not just for you but for everyone else working with your code.

- **any Types Mask Bugs When You Refactor Code**

```javascript
interface Component Props {
  onSelectItem: (item: any) => void;
}

// Here's code that manages that component:
function render Selector(props: ComponentProps) { /*...*/ }
let selectedId: number = 0;
function handleSelectItem(item: any) {
  selectedId= item. id;
}
renderSelector({onSelectItem: handleSelectItem});

//Later you rework the selector in a way that makes it harder to pass the whole item object through to onSelectItem. 
//But that's no big deal since you just need the ID. You change the signature in Component Props. It passed type checker but it produces runtime exception
interface Component Props { }
onSelectItem: (id: number) => void;
```

- **any Hides Your Type Design**

- **any Undermines Confidence in the Type System**

  - Every time you make a mistake and the type checker catches it, it boosts your confidence in the type system. But when you see a type error at runtime, that confidence takes a hit. If you're introducing TypeScript on a larger team, this might make your coworkers question whether TypeScript is worth the effort. any types are often the source of these uncaught errors.

  - TypeScript aims to make your life easier, but TypeScript with lots of any types can be harder to work with than untyped JavaScript because you have to fix type errors and still keep track of the real types in your head. When your types match reality, it frees you from the burden of having to keep type information in your head. TypeScript will keep track of it for you.


# Use Your Editor to Interrogate and Explore the Type System

- Take advantage of the TypeScript language services by using an editor that can use them.
Use your editor to build an intuition for how the type system works and how TypeScript infers types.

- Know how to jump into type declaration files to see how they model behavior.

- When you install TypeScript, you get two executables:
  - tsc, the TypeScript compiler
  - tsserver, the TypeScript standalone server

- configure the language services with your editor for services like autocomplete, inspection, navigation, and refactoring.

- if the inferred type does not match your expectation, you should add a type declaration and track down the discrepancy.

Seeing TypeScript's understanding of a variable's type at any given point is essential for building an intuition around widening (Item 21) and narrowing (Item 22). Seeing the type of a variable change in the branch of a conditional is a tremendous way to build confidence in the type system (see Figure 2-3).

```javascript
function logMessage(message: string | null) { 
  if (message) {
    // type of message is string | null outside the branch but string inside
    message
  }
}
```

```javascript
const foo = {
  //If your intention was for x to be a tuple type ([number, number, number]), then a type annotation will be required.
  //(property) x: number []
  x: [1, 2, 3],
  bar: {
  }
};
```

- Seeing type errors in your editor can also be a great way to learn the nuances of the type system. For example, this function tries to get an HTMLElement by its ID, or return a default one. TypeScript flags two errors:

```javascript
function getElement (el0rId: string| HTMLElement | null): HTMLElement { 
  if (typeof el0rId === 'object') { 
    // 'HTMLElement | null' is not assignable to 'HTMLElement'
    // The intent in the first branch of the if statement was to filter down
    // to just the objects, namely, the HTMLElements.
    // But oddly enough, in JavaScript typeof null is "object", 
    // so el0rId could still be null in that branch. 
    // You can fix this by putting the null check first. 
    return el0rId;
  } else if (el0rId === null) { 
    return document.body;
  } else {
    const el = document.getElementById(el0rId);
    // ~~~~~~~'HTMLElement | null' is not assignable to 'HTMLElement'
    // The second error is because document.getElementById can return null,
    // so you need to handle that case as well, perhaps by throwing an exception.
    return el;
  }
}
```
# think of types as sets of values

- Think of types as sets of values (the type's domain). These sets can either be finite (e.g., boolean or literal types) or infinite (e.g., number or string).

  - The smallest set is the empty set, which contains no values. It corresponds to the never type in TypeScript. Because its domain is empty, no values are assignable to a variable with a never type:

```javascript
const x: never = 12;
// Type '12' is not assignable to type 'never'
```

  - The next smallest sets are those which contain single values. These correspond to literal types in TypeScript, also known as unit types:

```javascript
type A = 'A';
type B = 'B';
type Twelve = 12;
// To form types with two or three values, you can union unit types:
type AB = 'A' | 'B'; 
type AB12 = 'A' | 'B' | 12;
// and so on. Union types correspond to unions of sets of values.
```
  - The word "assignable" appears in many TypeScript errors. In the context of sets of values, it means either "member of” (for a relationship between a value and a type) or "subset of" (for a relationship between two types):

  - At the end of the day, almost all the type checker is doing is testing whether one set is a subset of another

- Think of Identified interface as a description of the values in the domain of its type. Does the value have an id property whose value is assignable to (a member of) string? Then it's an Identified.

- Two ways of thinking of type relationships: as a hierarchy or as overlapping sets
- With the Venn diagram, it's clear that the subset/subtype/assignability relationships are unchanged if you rewrite the interfaces without extends:

- Typescript types form intersecting sets (a Venn diagram) rather than a strict hierarchy. Two types can overlap without either being a subtype of the other.
  - Remember that an object can still belong to a type even if it has additional properties that were not mentioned in the type declaration.

```javascript
interface Person { 
  name: string;
}
interface Lifespan {
  birth: Date;
  death? Date;
}
type PersonSpan = Person & Lifespan;
const ps: PersonSpan = {
  name: 'Alan Turing',
  birth: new Date('1912/06/23'),
  death: new Date('1954/06/07'), // OK
};
```

- Type operations apply to a set's domain. The intersection of A and B is the intersection of A's domain and B's domain. For object types, this means that values in A & B have the properties of both A and B.
  - Think of "extends," "assignable to," and "subtype of" as synonyms for "subset of."

```javascript
interface Point {
  x: number;
  y: number;
}
type PointKeys = keyof Point; // Type is "x" | "y"
function sortBy<K extends keyof T, T>(vals: T[], key: K): T[] {}
const pts: Point[] = [{x: 1, y: 1}, {x: 2, y: 0}];
sortBy (pts, 'x'); // OK, 'x' extends'x'|'y' (aka keyof T)
sortBy (pts, 'y'); // OK, 'y' extends 'x'|'y'
sortBy(pts, Math.random() < 0.5 ? 'x': 'y'); // OK, 'x', 'y' extends 'x'|'y'
sortBy (pts, 'z'); //Type "z" is not assignable to parameter of type "x"|"y"

```

- What's the relationship between string|number and string|Date, for instance? Their intersection is non-empty (it's string), but neither is a subset of the other. The relationship between their domains is clear, even though these types don't fit into a strict hierarchy.
  - Union types may not fit into a hierarchy but can be thought of in terms of sets of values

- Thinking of types as sets can also clarify the relationships between arrays and tuples. 

```javascript
const list = [1, 2]; // Type is number[] 

// Type 'number[]' is missing the following properties from type
// [number, number]': 0, 1
const tuple: [number, number] = list; 
//The empty list and the list [1] are list of numbers which are not pairs of numbers. It therefore makes sense that number [] is not assignable to [number, number] since it's not a subset of it. (The reverse assignment does work.)

//'[number, number, number]' is not assignable to '[number, number]' 
//Types of property 'length are incompatible
//Type '3' is not assignable to type '2'
const triple: [number, number, number] [1, 2, 3];
const double: [number, number] = triple; 
//TypeScript models a pairs of numbers as {0: number, 1: number, length: 2}.
```

- Finally, it's worth noting that not all sets of values correspond to TypeScript types. There is no TypeScript type for all the integers, or for all the objects that have x and y properties but no others. You can sometimes subtract types using Exclude, but only when it would result in a proper TypeScript type:

```javascript
type T = Exclude <string | Date, string| number>; // Type is Date
type NonZeroNums = Exclude <number, 0> ; // Type is still just number
```

# prefer type declarations to type assertions

- Prefer type declarations `(: Type)` to type assertions `(as Type)`.

```javascript
const alice: Person = {}; 
// type '{}' Property 'name' is missing in but required in type 'Person'
const bob = {} as Person; // No error
```

```javascript
interface Person { name: string };
const alice: Person = { name: 'Alice' }; // Type is Person
const bob = { name: 'Bob' as Person; } // Type is Person
// The first (alice: Person) adds a type declaration to the variable 
// and ensures that the value conforms to the type. 
// The latter (as Person) performs a type assertion. 
// This tells TypeScript that, despite the type it inferred,
// you know better and would like the type to be Person.

// The same thing happens if you specify an additional property:
const alice: Person = { 
  name: 'Alice',
  occupation: 'TypeScript developer' 
  // Object literal may only specify known properties
  // and 'occupation' does not exist in type 'Person'
};

const bob = {
  name: 'Bob', 
  occupation: 'JavaScript developer'
} as Person; // No error
```

- Know how to annotate the return type of an arrow function.

```javascript
//It's tempting to use a type assertion here, and it seems to solve the problem:
const people = ['alice', 'bob', 'jan']
.map(name => ({name} as Person)); // Type is Person[]


//But this suffers from all the same issues as a more direct use of type assertions.
//For example:
const people = ['alice', 'jan'].map(name => ({} as Person)); // No error

//A more concise way is to declare the return type of the arrow function:
const people = ['alice', 'bob', 'jan'].map((name): Person => ({name})); 
// Type is Person []
```

- Use type assertions and non-null assertions when you know something about types that TypeScript does not.

```javascript
//For instance, you may know the type of a DOM element more precisely than TypeScript does:
document.querySelector('#myButton')
.addEventListener('click', e => {
  e.currentTarget // Type is Event Target 
  const button = e.currentTarget as HTMLButtonElement;
  button // Type is HTMLButtonElement 
//Because TypeScript doesn't have access to the DOM of your page,
//it has no way of knowing that #myButton is a button element.
//And it doesn't know that the currentTarget of the event should be that same button.
//Since you have information that TypeScript does not,
//a type assertion makes sense here
});

//You may also run into the non-null assertion,
//which is so common that it gets a special syntax:
const elNull = document.getElementById('foo'); // Type is HTMLElement | null 
const el = document.getElementById('foo')!; // Type is HTMLElement
//Used as a prefix, ! is boolean negation.
//But as a suffix, is interpreted as an assertion that the value is non-null.
//You should treat ! just like any other assertion: 
//it is erased during compilation, 
//so you should only use it if you have information that the type checker lacks
//and can ensure that the value is non-null.
//If you can't, you should use a conditional to check for the null case.


interface Person { name: string; } 
const body = document.body; 
const el = body as Person;
//Conversion of type 'HTMLElement' to type 'Person' may be a mistake
//because neither type sufficiently overlaps with the other. If this was intentional,
//convert the expression to 'unknown' first
const el = document.body as unknown as Person; // OK
```

# Avoid Object Wrapper Types (String, Number, Boolean, Symbol, BigInt)

- Understand how object wrapper types are used to provide methods on primitive values. Avoid instantiating them or using them directly.

- While a string primitive does not have methods, JavaScript also defines a String object type that does. JavaScript freely converts between these types. When you access a method like charAt on a string primitive, JavaScript wraps it in a String object, calls the method, and then throws the object away.

- Avoid TypeScript object wrapper types. Use the primitive types instead: string instead of String, number instead of Number, boolean instead of Boolean, symbol instead of Symbol, and bigint instead of BigInt.

```javascript
// Don't do this!
const originalCharAt = String.prototype.charAt; 
String.prototype.charAt = function(pos) { 
  console.log(this, typeof this, pos);
  return originalCharAt.call(this, pos);
};
console.log('primitive'.charAt(3));

// This produces the following output:
[String: 'primitive'] object 3
m

// The this value in the method is a String object wrapper, not a string primitive. 
// You can instantiate a String object directly and it will sometimes behave like a string primitive. But not always. For example, a String object is only ever equal to itself:
"hello" === new String("hello") -> false
new String("hello") === new String("hello") -> false

// The implicit conversion to object wrapper types explains an odd phenomenon in JavaScript-if you assign a property to a primitive, it disappears:
> x = "hello"
> x.language = 'English' 'English'
> x.language undefined
Now you know the explanation: x is converted to a String instance, the language property is set on that, and then the object (with its language property) is thrown away.
There are object wrapper types for the other primitives as well: Number for numbers, Boolean for booleans, Symbol for symbols, and BigInt for bigints (there are no object wrappers for null and undefined).
```

- As a final note, it's OK to call BigInt and Symbol without new, since these create primitives:

# Using Either/Result in TypeScript for Error Handling

- from [fp-ts](https://gcanti.github.io/fp-ts/) library:

```typescript
import * as P from 'fp-ts/lib/pipeable';
import * as E from 'fp-ts/lib/Either';
import axios, { AxiosResponse, AxiosError } from 'axios';

// Custom error type
type ResponseError = string;

async function makeApiCall(): Promise<E.Either<ResponseError, AxiosResponse>> {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
    return E.right(response);
  } catch (error) {
    const axiosError = error as AxiosError;
    return E.left(`API Error: ${axiosError.response?.statusText || 'Unknown'}`);
  }
}

const post = makeApiCall()
  .then((apiResponse) => {
    P.pipe(
      apiResponse,
      E.match(
        (error: ResponseError) => {
            console.error(error);
            return null
        },
        (response: AxiosResponse) => response.data
      )
    );
  });
```

- or we can use [custom result](./result.ts) type
- [either/result for error handling](https://blog.devgenius.io/using-either-result-in-typescript-for-error-handling-66baceefd9a0)
- [ts-pattern](https://github.com/gvergnaud/ts-pattern)
- [@flagg2/result](https://github.com/flagg2/result)

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

- don't be tempted to replace nullable properties with promises. This tends to lead to even more confusing code and forces all your methods to be async. Promises clarify the code that loads data but tend to have the opposite effect on the class that uses that data.

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
