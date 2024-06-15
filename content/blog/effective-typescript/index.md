---
title: effective typescript summary - wip
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

# Recognize the Limits of Excess Property Checking 

- When you assign an object literal to a variable or pass it as an argument to a function, it undergoes excess property checking.
- Excess property checking is an effective way to find errors, but it is distinct from the usual structural assignability checks done by the TypeScript type checker. Conflating these processes will make it harder for you to build a mental model of assignability.
- Be aware of the limits of excess property checking: introducing an intermediate variable will remove these checks.

```ts
//When you assign an object literal to a variable with a declared type, TypeScript makes sure it has the properties of that type and no others:
//you've triggered a process known as "excess property checking," which helps catch an important class of errors that the structural type system would otherwise miss
interface Room {
  numDoors: number;
  ceilingHeightFt: number;
}
const r: Room = {
  numDoors: 1,
  ceilingHeightFt: 10,
  elephant: 'present',
  //~`Object literal may only specify known properties, and 'elephant' does not exist in type 'Room'
};

//The elephant constant is assignable to the Room type, which you can see by introducing an intermediate variable:
//The type of obj is inferred as { numDoors: number; ceilingHeightFt: number; elephant: string}. Because this type includes a subset of the values in the
//Room type, it is assignable to Room, and the code passes the type checker
const obj = {
  numDoors: 1, 
  ceilingHeightFt: 10,
  elephant: 'present',
};
const r:
Room = obj; // OK, as the right hand side is not object literal

//TypeScript goes beyond trying to flag code that will throw exceptions at runtime. It also tries to find code that doesn't do what you intend. Here's an example of the latter:
interface Options {
  title: string;
  darkMode?: boolean;
}

function createWindow(options: Options) {
  if (options.darkMode) {
    setDarkMode();
  }
  // ...
}

createWindow({
  title: 'Spider Solitaire',
  darkmode: true
  // Object literal may only specify known properties, but 'darkmode' does not exist in type 'Options'.
  // Did you mean to write 'darkMode'?
});


// Excess property checking does not happen when you use a type assertion:
const o = { darkmode: true, title: 'Ski Free' } as Options; // OK
// This is a good reason to prefer declarations to assertions

// If you don't want this sort of check, you can tell TypeScript to expect additional properties using an index signature:
interface Options {
  darkMode?: boolean;
  [otherOptions: string]: unknown;
}
const o: Options = { darkmode: true }; // OK


//A related check happens for "weak" types, which have only optional properties:
interface LineChartOptions (
  logscale?: boolean;
  invertedYAxis?: boolean;
  areaChart?: boolean;
}
const opts = { logScale: true };
const o: LineChartOptions = opts;
// ~ Type '{ logScale: boolean; }' has no properties in common // with type 'LineChartOptions'
//For weak types like this, TypeScript adds another check to make sure that the value type and declared type have at least one property in common.
```


# Apply Types to Entire Function Expressions When Possible

## Things to Remember

- Consider applying type annotations to entire function expressions, rather than to their parameters and return type.
- If you're writing the same type signature repeatedly, factor out a function type or look for an existing one.
- If you're a library author, provide types for common callbacks.
- Use `typeof fn` to match the signature of another function, or `Parameters` and a rest parameter if you need to change the return type.


## Code Samples

```ts
function rollDice1(sides: number): number { /* ... */ }  // Statement
const rollDice2 = function(sides: number): number { /* ... */ };  // Expression
const rollDice3 = (sides: number): number => { /* ... */ };  // Also expression
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAJzgGzQERhApgRgAoBnGAE12IC5EwQBbAI12QEoa6mXEBvRAegBUiAMIB5ALIAFAEoBRAMoLEg-ilxQQyJAAYA3AOFyAcphVqAvogFqFUAIZRc9XGCgAoCAmJQU6LDi4AEyIALyIoJCwCCTklBwMzGwJXMi8hqKSsorKquqa2oj6GSZmeRYGNohyAB4ADsiUpAie3r6oGNh4AMxhiLEU1LSJLOzDqWEAfOlCmdLySub5WroGs6VLFdb8agCCaMRwiLj1jcTNYO7uQA)

----

```ts
type DiceRollFn = (sides: number) => number;
const rollDice: DiceRollFn = sides => { /* ... */ };
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAIglgYwgJQPYBt0DEB2UC8UAFAM5wAmEJAXFDgK4C2ARhAE4CUBAfHU62wDcAKASocJYFDYZ08JLXkpZuAlDKUSPKAG8oAegBUUAMIB5ALIAFZAFEAyvaiH90iMHps8ABkEHjtgByMM6uAL4iwkA)

----

```ts
function add(a: number, b: number) { return a + b; }
function sub(a: number, b: number) { return a - b; }
function mul(a: number, b: number) { return a * b; }
function div(a: number, b: number) { return a / b; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAQwCaoBTIFyLCAWwCMBTAJwBpEjd9jyBKRAb0TJKhDKWUQGpqAbkQBfAFChIsBIgDOIIllqFSlasvpkmrdp24pEAWiGiJ4aPCQEQAGyV4V5KjQebtbDlx6IAVCfGSFjKoMABu9nSqzhqq7rpeBgD0-mJAA)

----

```ts
type BinaryFn = (a: number, b: number) => number;
const add: BinaryFn = (a, b) => a + b;
const sub: BinaryFn = (a, b) => a - b;
const mul: BinaryFn = (a, b) => a * b;
const div: BinaryFn = (a, b) => a / b;
//reduced type annotations and makes the logic more apparent
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAQglgOwIYCcQDEFQLxQBRIBcUCArgLYBGEKANFJcWVTQJQ4B8JF1KA3ACgAxgHsEAZ2BQkAExnF4yNJhz4k9Su2xckUANQNBoiVPGlGsRKgxZcBDVp1QAtIeFjJUcqQA2Cq8q2ag6c0lAAVG7GnjJwAG7+Sjaq9gyOYQD0bkA)

----

```ts
declare function fetch(
  input: RequestInfo, init?: RequestInit,
): Promise<Response>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/CYUwxgNghgTiAEAzArgOzAFwJYHtVJAzAAsAKAKHni1QAdkMAueAJRAEdkQBnDASVSIcAGmqosGAPzM2nHv3EZh5AJTMACjBwBbLNxAAeNt1p59APgDc5IA)

----

```ts
async function checkedFetch(input: RequestInfo, init?: RequestInit) {
  const response = await fetch(input, init);
  if (!response.ok) {
    // An exception becomes a rejected Promise in an async function.
    throw new Error(`Request failed: ${response.status}`);
  }
  return response;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/IYZwngdgxgBAZgV2gFwJYHsIygCwKZQDWeAJgGJ7K4AUqEADgsgFwwBKeAjgniMgJIQ46ADQw6qZAH5WHbrwERJAShgBvAFAxsmPjABOverrwwAvDGAB3YJPiUadRsjETkygNxbxcGNQCEhiDGECB4AHTohKqa2toA9PEwAIJYeAAeUHj0aJgwAEYE6AC2vJYGeABWBMikMAAK+iWoYeJYwO3g0PBIULkQ4d7ayDhNVjAQeOMAovpN+tQABnI8enC2ADakrAAkakEhYeF8wMgIIAC+i57eF96GZ-pYByZed0A)

----

```ts
// we've changed from a function statement to a function expression and applied a type (typeof fetch) to the entire function. This allows TypeScript to infer the types of the input and init parameters.
const checkedFetch: typeof fetch = async (input, init) => {
  const response = await fetch(input, init);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMAWBTYBrRATAYoqCBcMUAngA6IgBmMFOCMAvDAIYRFjAwAUAlmCQK5QANDF7coASgYA+GAG8AUDDjhoMAE6IIJVYgbMA7k3HVa8Hn0EixkgNxLRVTgEJN23QDoQKKYuXKoeHUQAxgwRFCAUXVg9U4AAwAlRABHfi1YCmMAGwwCABI5Nx1IRA9oJih+CABfeIl7ZRqHTSr1MA0tEohEe2agA)

----

```ts
const checkedFetch: typeof fetch = async (input, init) => {
  //  ~~~~~~~~~~~~
  //  'Promise<Response | HTTPError>' is not assignable to 'Promise<Response>'
  //    Type 'Response | HTTPError' is not assignable to type 'Response'
  // The type annotation also guarantees that the return type of checkedFetch will be the same as that of fetch.
  // by changing the throw to return, typescript caught the mistake as above
  const response = await fetch(input, init);
  if (!response.ok) {
    return new Error('Request failed: ' + response.status);
  }
  return response;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMAWBTYBrRATAYoqCBcMUAngA6IgBmMFOCMAvDAIYRFjAwAUAlmCQK5QANDF7coASgYA+GAG8AUDBgB6FcoB+W7Tq1LV6mAHIACgCcQAW24REAHgBKiCCXC2YAHxgAJACq+TAFEzCzNpI1EIGDAQWBYIbgBzMCYAIwAbREIQY3MrG3snFzdEcP01ZWVfUiyjItdILK8-AODQiJto2OYIBOS0zOzCGuN6kqN9UEhYM2cG90YmAHcmcWpaeB4+QRExSQBufW4qTgBCWeLGgDoQFClFSphZqH4zMGjEJZg2kDNOOsQAEd+M5YBRVpl0AQIgBqJ5zEpXaBMF4QCSHZQAX30z1e7wu80Qh2xQA)

----

```ts
//what if you want to match the parameter types of another function but change the return type? This is possible using a rest parameter and the built-in Parameters utility type
//you also benefit from this technique whenever you pass a callback to another function. When you use the map of filter method of an Array, for example, TypeScript is able to infer a type for the callback parameter, and it applies that type to your function expression.
async function fetchANumber(
    ...args: Parameters<typeof fetch>
): Promise<number> {
  const response = await checkedFetch(...args);
  const num = Number(await response.text());
  if (isNaN(num)) {
    throw new Error(`Response was not a number.`);
  }
  return num;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMAWBTYBrRATAYoqCBcMUAngA6IgBmMFOCMAvDAIYRFjAwAUAlmCQK5QANDF7coASgYA+GAG8AUDBgB6FcoB+W7Tq1LV6mAHIACgCcQAW24REAHgBKiCCXC2YAHxgAJACq+TAFEzCzNpI1EIGDAQWBYIbgBzMCYAIwAbREIQY3MrG3snFzdEcP01ZWVfUiyjItdILK8-AODQiJto2OYIBOS0zOzCGuN6kqN9UEhYM2cG90YmAHcmcWpaeB4+QRExSQBufW4qTgBCWeLGgDoQFClFSphZqH4zMGjEJZg2kDNOOsQAEd+M5YBRVpl0AQIgBqJ5zEpXaBMF4QCSHZQAX30z1e7wu80Qh2xLDYHAo-HYUG44HWuHgAEEAHL8SypRB-fTKK48phmRIQAgmPlMSw4DkQOzEMiUOkIaQKCRCizWWx2MCs9lheSTNwzBGNBjMFZrBDINBYDacHlXPkC9G66bRVlGllsjmcZarfWXWxXKCIAAeUE4EgdymOXBsTKYTM4GssYZ1jyg8AsXzAn2+IV+nAABmNDSsojE4s73WYrnnwzBscpcW9y8SFEA)

----

```ts
fetchANumber
// ^? function fetchANumber(
//      input: RequestInfo | URL, init?: RequestInit | undefined
//    ): Promise<number>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMAWBTYBrRATAYoqCBcMUAngA6IgBmMFOCMAvDAIYRFjAwAUAlmCQK5QANDF7coASgYA+GAG8AUDBgB6FcoB+W7Tq1LV6mAHIACgCcQAW24REAHgBKiCCXC2YAHxgAJACq+TAFEzCzNpI1EIGDAQWBYIbgBzMCYAIwAbREIQY3MrG3snFzdEcP01ZWVfUiyjItdILK8-AODQiJto2OYIBOS0zOzCGuN6kqN9UEhYM2cG90YmAHcmcWpaeB4+QRExSQBufW4qTgBCWeLGgDoQFClFSphZqH4zMGjEJZg2kDNOOsQAEd+M5YBRVpl0AQIgBqJ5zEpXaBMF4QCSHZQAX30z1e7wu80Qh2xLDYHAo-HYUG44HWuHgAEEAHL8SypRB-fTKK48phmRIQAgmPlMSw4DkQOzEMiUOkIaQKCRCizWWx2MCs9lheSTNwzBGNBjMFZrBDINBYDacHlXPkC9G66bRVlGllsjmcZarfWXWxXKCIAAeUE4EgdymOXBsTKYTM4GssYZ1jyg8AsXzAn2+IV+nAABmNDSsojE4s73WYrnnwzBscpcW9y8SFDR6czNRyFBUAHoAfmolOA1NprYQ7YrnC7hkevAEUAITmBoIAkmAKDkvABVBwAGV2YHEvYXQJB0FXay8lPQiAovAwU8eSpgeVV9gTWoVQA)


# Know the Differences Between type and interface

## Things to Remember

- Understand the differences and similarities between `type` and `interface`.
  - for new code where you need to pick a style, the general rule of thumb is to use interface where possible, using either where it's required, (e.g, union types) or has a clearer syntax (e.g. function types)
- Know how to write the same types using either syntax.
- Be aware of declaration merging for `interface` and type inlining for `type`.
- For projects without an established style, prefer `interface` to `type` for object types until you need to use features from type. Otherwise, stick with established styles
- for complex types, you need to use type alias. For function types, tuple types, and array types, the type syntax is more concise and natural than the interface syntax.
- you can enforce consistent use of type or interface using typescript-eslint's consistent type-definitions rule.

## Code Samples

----

```ts
// this type alias form (TFn) looks more natural and is more concise for function types. This is the preferred form and is the one you're most likely to encounter in type declarations.
type TFn = (x: number) => string;


// the latter 2 forms reflect the fact that functions in javascript are callable objects.
interface IFn {
  (x: number): string;
}
type TFnAlt = {
  (x: number): string;
};

const toStrT: TFn = x => '' + x;  // OK
const toStrI: IFn = x => '' + x;  // OK
const toStrTAlt: TFnAlt = x => '' + x;  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAKgysAhsaBeKBvAUFKA7RAWwgC4oBnYAJwEs8BzAbhygGNEwakAbMy2hswC+zOiioAzRK2gBJBMmjZcBYn2p0mLdpx7qBWoVlCRYAMTxR0ACgAeZPAFdCAIwhUAlFYB8FDYKwxdykZKFkLTBY7B2c3T31NYWNwaBgLAEFuYCtI3Gj8WPcPBICRLCxWAHs8SihgSoQqGDI0y3RbHygAci6oAGooW0ZcAHoRqAB5AGkK6tr6xtkycLbBzp7+weGoMcmZqprsheoYTOAWjKycjtRfDYGh0fHprCA)


----

```ts
// an interface can extend a type, and a type can extend an interface
interface IStateWithPop extends TState {
  population: number;
}

// you can't extend union type, if you want to do that, you'll need to use type and &
type TStateWithPop = IState & { population: number; };
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAKgysAhsaBeKBvAUFKA7RAWwgC4oBnYAJwEs8BzAbhygGNEwakAbMy2hswC+zOiioAzRK2gBJBMmjZcBYn2p0mLdpx7qBWoVjERJ0uQpQB1LgAsACgHswUCAA8UeACblYlpSxgzgCu3Mg0jnhkeMGEAEamwligkH5I1nZOLujy6dAAZJhQQWCh4ZHRsQlUjFAiWEA)

----

```ts
// class can implement either an interface or a simple type
class StateT implements TState {
  name: string = '';
  capital: string = '';
}
class StateI implements IState {
  name: string = '';
  capital: string = '';
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAKgysAhsaBeKBvAUFKA7RAWwgC4oBnYAJwEs8BzAbhygGNEwakAbMy2hswC+zOiioAzRK2gBJBMmjZcBYn2p0mLdpx7qBWoVlbdE5clAUoYUGoTDcIxPMAvwkKTC1WkKGhlDoAORBzLg6XIi8fgaBUCHCxqbmlh4Qsrb2js6uUPJpXipEvvyacQnaHJHRpQHBoVhGQA)

----

```ts
// there's union type but no interface
type AorB = 'a' | 'b';
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAgg9gJwEJQLxQOQEMNQD6YBGGA3AFBA)

----

```ts
type Input = { /* ... */ };
type Output = { /* ... */ };
interface VariableMap {
  [name: string]: Input | Output;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAkgdmArsKBeKBvKB6AVFAOiKl2ygF8BuAKFEigHlkkV0s9DjSKaBLOYBABOAMwCGAY2gA1MUN5iARgBsIAWTFhM1KFADacMQFsIALigBnYPLgBzALrn4LKAB9GzZDXLUgA)

----

```ts
type NamedVariable = (Input | Output) & { name: string };
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAkgdmArsKBeKBvKB6AVFAOiKl2ygF8BuAKFEigHlkkV0s9DjSKaBLOYBABOAMwCGAY2gA1MUN5iARgBsIAWTFhM1KFADacMQFsIALigBnYPLgBzALrn4LKAB9GzZDXK1w0AHLGEAAmsvJKqmhQABTOyG4ewCwAlFAAZJhQhibmVja2PNRAA)

----

```ts
interface Person {
  name: string;
  age: string;
}

type TPerson = Person & { age: number; };  // no error, unusable type

interface IPerson extends Person {
  //      ~~~~~~~ Interface 'IPerson' incorrectly extends interface 'Person'.
  //                Types of property 'age' are incompatible.
  //                  Type 'number' is not assignable to type 'string'.
  // generally you want more safety check, so this is a good reason to use extends with interfaces
  age: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyIcAthAFzIZhSgDmA3EcnA1TXYywL4EEwATwAOKACroo2XAF40mHMgBk+Nh2ogArmQBG0Jsl6HkAelMksyaFCxQANMi3aMcXQBsUwsQNCRYiCgAklIy1gAekCAAJhgK0kqExObEqcgAfplZ6chB4NDwSMgA5CGKIMXIoAh2UBAIYO5CEVGxVfkBRcWhOMUAdKwpacMj4qIQcVgwyCK2YlDCJewQlXB17TVkInBgwB4QA8kWIydpY2Il2nrQlcBxIFhgbBgYwAyk+8hgVt4oxbT0EAMfqsZaaHT6KB8AhAA)

----

```ts
// type aliases are the natural way to express tuple and array types
type Pair = [a: number, b: number];
type StringList = string[];
type NamedNums = [string, ...number[]];
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBACghgSwE5QLxQNpwFxQHYCuAtgEYRIA0UJuhp5AugNwBQokUAysEgngOYAZBAGdgaKGN4CMzNuGgA5OEQgATRcRESMUvvyoA6Y3TJJZcoA)

----

```ts
// this is known as "declaration merging"
// typescript itself uses declaration merging to model the different versions of javascript's standard library
// declaration makes most sense in declaration files. It can happen in user code, but only if the two interfaces are defined in the same module (i.e: the same .ts file). This prevents accidental collisions with global interfaces with generic-sounding names like Location and FormData
interface IState {
  name: string;
  capital: string;
}
interface IState {
  population: number;
}
const wyoming: IState = {
  name: 'Wyoming',
  capital: 'Cheyenne',
  population: 578_000
};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgJIGUx0sg3gKGWRDgFsIAuZAZzClAHMBuQ5BOAB2CwBsrb6IZvgC++UJFiIUGLDgJEOAew4BXHtmBKQVEKtIAjaCzEJttZAHcAnktKMqs7CgC8eViXJUA5AHVb9kLeADSs7Fy8PgDCABYQ1hAgIBAhrMpqGmBaOsgArADsABwA+gAM5aJMRAD01cgA8gDS+EA)

----

```ts
//TypeScript will always try to refer to an interface by its name, whereas it takes more liberties replacing a type alias with its underlying definition.
export function getHummer() {
  type Hummingbird = { name: string; weightGrams: number; };
  const ruby: Hummingbird = { name: 'Ruby-throated', weightGrams: 3.4 };
  return ruby;
};

const rubyThroat = getHummer();
//    ^? const rubyThroat: Hummingbird
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/KYDwDg9gTgLgBAMwK4DsDGMCWEVwObAwASSAtqcFABQCUcA3gFBxwwCeYwcJ5mKeAI0xQAJnAC8DOCgCGFAFxwAzjCh88AbjgB3YJjwALGAHEocpYpRkBlLQF8NzOGhwq4UJALaKepdUNEJKVkFOAByACVPNgBaGAMoCBkYYBEwgBodPUMTM1ILOABmADoAFjgHJyhCJChcDy9HSsYXFDcGtgAVBKT4SQJiMgpqGkcAejGWFgA9AH5nV3gO7sTknyH-YRFGIA)

----

```ts
// get-hummer.d.ts
export declare function getHummer(): {
  name: string;
  weightGrams: number;
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEHMFMBcFoAsCuBbZkBOA6AJp6BnAKEgA8AHAe3WlG0gGMAbAQ3UlADNEA7e6ASwrcIMABIo06ABQBKAFygA3oVChuzNAvzR0-buADcK0AHdI-cPGgBxdBvwLuKAEYYjAXyNA)

----

```ts
export function getHummer() {
  //            ~~~~~~~~~
  // Return type of exported function has or is using private name 'Hummingbird'.
  interface Hummingbird { name: string; weightGrams: number; };
  const bee: Hummingbird = { name: 'Bee Hummingbird', weightGrams: 2.3 };
  return bee;
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&declaration=true#code/KYDwDg9gTgLgBAMwK4DsDGMCWEVwObAwASSAtqcFABQCUcA3gFBxwD0rLnXnAfn--2ZsOAJUJIouGAE8wwOBARxQkWMAAmiVBmy4AFgEMAzgqhxMJpEcwo8cMFEwA3AzHkoDFOAHIS5G3gARphQ6t4AdEI2blAIBmjyfqQBwaEMcB4UAFxwRjCOtgDccADuwJh4ejAA4lCeRjkoZIGUxQC+hUJoOHlwLcA5SSkhmgC86ZkDPgBCwIlkybapYQA0peWVNXWkDXAATOEAzHAdQlDikn1znadAA)


# Use readonly to Avoid Errors Associated with Mutation

## Things to Remember

- If your function does not modify its parameters, declare them `readonly` (arrays) or `Readonly` (object types). This makes the function's contract clearer and prevents inadvertent mutations in its implementation.
- Understand that `readonly` and `Readonly` are shallow, and that `Readonly` only affects properties, not methods.
- Use `readonly` to prevent errors with mutation and to find the places in your code where mutations occur.
- Understand the difference between `const` and `readonly`: the former prevents reassignment, the latter prevents mutation.



## Code Samples

```ts
interface PartlyMutableName {
  readonly first: string;
  last: string;
}

const jackie: PartlyMutableName = { first: 'Jacqueline', last: 'Kennedy' };
jackie.last = 'Onassis';  // OK
jackie.first = 'Jacky';
//     ~~~~~ Cannot assign to 'first' because it is a read-only property.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgApymANgTwLICuYcARlhAHJwC2KA3gFDLJQRwAmA9iLsjMFADOYAFzJhUUAHMA3E2RY4wsROlyAvgwYJuw5ACtEAa2AQx6TLkLEylGigC8yOnwHLkAcgBSiAI4EILFAIDwAaBSVRTwBpCBAQCHYcD2R1OUMEEwgAOkU9Jw8AeRAlQWBBDxlmAHpq5ELohgys7P4hMGQCn0zkuVrmAYA-YeHkAGE4eM4O0uApEGQwTk824RSSCAQ4AkEUYA7y5DgWNnYAWm5eAAcoTivoMBxshiA)

----

```ts
interface FullyMutableName {
  first: string;
  last: string;
}
type FullyImmutableName = Readonly<FullyMutableName>;
//   ^? type FullyImmutableName = {
//        readonly first: string;
//        readonly last: string;
//      }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGIFcA2mCeBZdMOAI0wgDk4BbFAbwChlkZgoBnMALmQ6lAHMA3I2SY4HbrwHCAvvTA4ADigzYcASSpVCJMpRrIAvMgBKEOABMA9iFwAeVbgJFSFahAB8wgPTemyAD0AfmQFZTQsXE1tFz13I2QGX38U5Chza1scZlYJHjA+ECF6ZNSmdMsbXFFxLnzC4tKUuSA)

----

```ts
interface Outer {
  inner: {
    x: number;
  }
}
const obj: Readonly<Outer> = { inner: { x: 0 }};
obj.inner = { x: 1 };
//  ~~~~~ Cannot assign to 'inner' because it is a read-only property
obj.inner.x = 1;  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nhAA)

----

```ts
type T = Readonly<Outer>;
//   ^? type T = {
//        readonly inner: {
//          x: number;
//        };
//      }
// there's no built-in support for deep readonly types, may need to use DeepReadonly generic in ts-essentials
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nhtLcgAKs7ScrVqmNAa3r6EAHoA-IlKkzO6+MNUxxXzIMr6hsZ4R8fHrvTMbDdrd54vb1xAA)

----

```ts
const date: Readonly<Date> = new Date();
date.setFullYear(2037);  // OK, but mutates date!
//Readonly  only affects properties. If you apply it to a type with methods that mutate the underlying object, it won't remove them
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nh8gsKycJBSlbUqACIzEFq6JADuyMuQABQAlOzTkHb5YABi6AoKAJoyULsATGYAzADsh0O+qCMANFmYZAMTArErHCAAQjwQA)

----

```ts
interface Array<T> {
  length: number;
  // (non-mutating methods)
  toString(): string;
  join(separator?: string): string;
  // ...
  // (mutating methods)
  pop(): T | undefined;
  shift(): T | undefined;
  // ...
  [n: number]: T;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nigWPBIyACCUFBwqgAqWviEChAgsWAAFnSMLFDsQ74AFCD8VQyYcGCgscgMELu8sgIAlJRJAMpgUPend7kIT-LbHZBiXigU75epwBZJKAAfmBf3uQOQIPu4OGdjxlGGp2uYFu90ezx2rw+lHqzUB5CWyAAPsh0CBZBAYKAILJwQIdsAYGB6chGSy2RyuSReQTfHi7JQANogfbMaAAXQZ7C4QA)

----

```ts
interface ReadonlyArray<T> {
  readonly length: number;
  // (non-mutating methods)
  toString(): string;
  join(separator?: string): string;
  // ...
  readonly [n: number]: T;
}
//the key diffdrences are that the mutating methods (such as pop and shift) aren't defined on ReadonlyArray, and the two properties, length and index type ([n: number]: T), have readonly modifiers. This prevents resizing the array and assigning to elements in the array
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nigWPBIyNJytQCCUFBwqgAqWviEFXMgysgKECCxYAAWdIwsUOxDvgAUIPxVDJhwYKCxyAwQp7yyAgCUlCSAGUwFB3rd-uQhOCjtdkGJeKBbvl6nBlkkoAB+aFg95Q5Aw97w4Z2MmUbbyXZ1ADaIHOzGgAF1yKt2FwgA)

----

```ts
const a: number[] = [1, 2, 3];
const b: readonly number[] = a;
const c: number[] = b;
//    ~ Type 'readonly number[]' is 'readonly' and cannot be
//      assigned to the mutable type 'number[]'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0nh8gpF0jCxQANoAus5zbgA0yABM6wDMC+wTQlnkFXK1yPTM0IvOcPv8hwjTl-NLukzevlR+yAAqSi2pE7yEDKc4zK4LTLFQGVWqZMKyZA5cLCFh4YZUQhRGLxCCIpKJAAWKAYmDgTAUKDaAJSF1mixSeCAA)

----

```ts
function printTriangles(n: number) {
  const nums = [];
  for (let i = 0; i < n; i++) {
    nums.push(i);
    console.log(arraySum(nums as readonly number[]));
    //                   ~~~~~~~~~~~~~~~~~~~~~~~~~
    // The type 'readonly number[]' is 'readonly' and cannot be
    // assigned to the mutable type 'number[]'.
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIFdJWQbwFDLKgjQBcuBhyAHuSOgLYBG0A3JQL55cID2IAZzDJeTAFbkAShDgATfgBsAngB4MWAHzIAvLiIgSUcjhrkADMg4d2osQDpi0HXtrIAjJfYB6L4QB+AQHIAMJwBrzCcAICwADmIMhgvMgA5I5QKcgsCHDoAijAwsACyHDIUDKyALSKSsgADlC89dBgSni2DgbQdtTObqyEPmgA0ngw6CAIYMD8pVBQcEoAyowAFHALdIwsUADaALoAlBSEChDCAozOZgA0yPQM7IQA7gAWwOfIa2uPzptQOz1ZprI4nACE2l0k1kEBgoAgshO+CoyCuDGQAGpdI9npZKBUwOgoAl0ewuBMpjM5o1QGAACpQYBhWLnAS-bbMaDIyh8QTCR4lXSHPEwXjYNbnIo3QbAZAqB6yzGYnmowVAvJvNbAI54wh8gS8c52BS8WIbBZLVYMX6MEpRcqVWoPHbQQ5gvXIYaon2+qiBAOBoPByhDXz0t4oNotVIVOTOx67Q6ZYqxp0gZSZMKyZA5cLCFihr2+KIxeKIxLJMCR5AMTBwJhfaMoFKJt0HFJ2TjcPBAA)

----

```ts
function arraySum(arr: readonly number[]) {
  let sum = 0, num;
  while ((num = arr.pop()) !== undefined) {
    //              ~~~ 'pop' does not exist on type 'readonly number[]'
    sum += num;
  }
  return sum;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAQwE6uQTwMogLYAUaqAXIqgKbIAmCANpomPgEYWoDaAugJSIDeAKESI6FKIgDO+RAF5EABgA0TfAG5hiAO4ALGGMQECzPHJToAdAAc4Vgjz4BCWfPDUKwGGArU+QkSIA9IEBoWEiAH5RiADkNlYxiLQUkkxwEhQAHjCSEgiIUJhWFLGUNPSMJmycXDGaItKmANTyJhoiAL6alFAgqEiNGl1AA)

----

```ts
function arraySum(arr: readonly number[]) {
  let sum = 0;
  for (const num of arr) {
    sum += num;
  }
  return sum;
}
//when you give a parameter a read-only type (either readonly for an array or Readyonly for an object type), a few things happen
// - Typescript checks that the parameter isn't mutated in the function body
// - you advertise to callers that your function doesn't mutate the parameter
// - callers may pass your function a readonly array or Readonly object.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwE4zFAKughmAcwBsBTAZwAowAuRMEAWwCMTUBKRAbwChFEIEZKHUZlEAXkQBtALoBuXomBxUiCqWEwJiAAxzEWgDx19MANRmOPPn3oMyAOmQgyACwow2Cm-0FxSDkRwBBS4qKi4AJ4AyoxUomxeigC+3KmgkLAIiGERMXG5tKgkuAAmCESRIsysslaKGohkjNp6isqqFAJgQtWIcMA54fU+zQyIZpJ23oipfMVQIKhIYwqpQA)


# Use Type Operations and Generic Types to Avoid Repeating Yourself

## Things to Remember

- The DRY (don't repeat yourself) principle applies to types as much as it applies to logic.
- Name types rather than repeating them. Use `extends` to avoid repeating fields in interfaces.
- Build an understanding of the tools provided by TypeScript to map between types. These include `keyof`, `typeof`, indexing, and mapped types.
- Generic types are the equivalent of functions for types. Use them to map between types instead of repeating type-level operations.
- Familiarize yourself with generic types defined in the standard library, such as `Pick`, `Partial`, and `ReturnType`.
- Avoid over-application of DRY: make sure the properties and types you're sharing are really the same thing.


## Code Samples

```ts
// the simplest way to reduce repetition is by naming your types
function distance(a: {x: number, y: number}, b: {x: number, y: number}) {
  return Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAExgZygQ0gUwBSYBciA3gB7FggC2ARjgE4A0iAnpTfQwL4u3HkOdRi3aIqwngEpSAKESIGOKCAZIAspigALAHRoAjgyh4CusogC0iWuZkAqe4gBMiANSIzrKzd2sHTs5SANyy3LJAA)

----

```ts
interface Point2D {
  x: number;
  y: number;
}
function distance(a: Point2D, b: Point2D) { /* ... */ }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgAoHtRgEwBFkDeAUMsgB4BcyIArgLYBG0A3CcgJ5W2MtEC+RGDRAIwwdCGQATYAGcwcERAAUcKhix4ANMgbrM4PAEpCyAPQAqZADpbyC2eQCgA)


----

```ts
// if several functions share hte same type signature, you can factor out a named type for this signature
type HTTPFunction = (url: string, opts: Options) => Promise<Response>;
const get: HTTPFunction = (url, opts) => { /* ... */ };
const post: HTTPFunction = (url, opts) => { /* ... */ };
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgCWA7ALgUwE4DMCGBjdUAeQAdVEB7ZAZ1AG8BfeEUWAOWnlQE9SjwAFUEAFAGIBXZPgrVQAXlAAKCZgA2ALlA1UmFAHMANKErkaWsrNoBKBQD5QIzJQC2iGugA8AJXQ1S1B52ANzw+IGooProqFpCopLSVgrKqmrGpqg0tvIO9KDAAFSgAMLEALIi3rAAyjWghWCYMarIjs5uHgB0zTSUagBu6ErI6ADuoL7+gcPW1sEFxRzQDWCMoeG0kQE6ccLiUjJUbYoq6hlmOXmLpRVVtfWNoM2ore2u7ug9fv1DI+OTPwBWizeY3ZarUDreDwIA)

----

```ts
interface Person {
  firstName: string;
  lastName: string;
}

interface PersonWithBirthDate extends Person {
  birth: Date;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyMwUGYAcnALYQBcyFUoA5gNxHIA2cF1dRszacAvgQKhIsRCnTkcAdWBgAFgCEyagCJxIyCAA9IIACYY0mHPi4AjLasa7IYgkA)


----

```ts
interface Vertebrate {
  weightGrams: number;
  color: string;
  isNocturnal: boolean;
}
interface Bird extends Vertebrate {
  wingspanCm: number;
}
interface Mammal extends Vertebrate {
  eatsGardenPlants: boolean;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyMwUGYAcnALYQBcyFUoA5gNxHIA2cF1dRszacAvgVCRYiFADVokAEZQ4kfFwDuEYKwAWYAOIqaGRiACuNRdE7EEWblihCwLEBy7AMlLAjDmoEDhuRkUsBwg4EDEJcGh4JGQAITIAE2QIAA9IEFSMZHkoJRU1QmINNgwAByiAYRozS2soGMl4mWQAWVoaYIzsiFz8wuLVFDKM1QwDOChUwdRecFNkMIiomKA)

----

```ts
type PersonWithBirthDate = Person & { birth: Date };
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyMwUGYAcnALYQBcyFUoA5gNxHIA2cF1dRszacAvgTABPAA4p05HAHVgYABYAhMmoAicSMgC8aTDmQAyfMgBGW1Y137RnIA)

----

```ts
interface State {
  userId: string;
  pageTitle: string;
  recentFiles: string[];
  pageContents: string;
}
interface TopNavState {
  userId: string;
  pageTitle: string;
  recentFiles: string[];
  // omits pageContents
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5AVwGdoBJAEwC5liwpQBzAbn2QAc5GIAVYMADYQadBiBZsoEJOABiwIcRH0mAbQC6rAp24BhAPbgI4JbRXjWAX1yhIsRCh772AOTgA3dJhR4CJctRmYhLaXLz8QsrBWshSMmDyilFqmmwA9GnI+gC2-MQcYQZGJrjWQA)

----

```ts
interface TopNavState {
  userId: State['userId'];
  pageTitle: State['pageTitle'];
  recentFiles: State['recentFiles'];
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5AVwGdoBJAEwC5liwpQBzAbn2QAc5GIAVYMADYQadBiBZsoEJOABiwIcRH0mAbQC6rAp24BhAPbgI4JbRXjWAX1yhIsRCh772AOTgA3dJhR4CJctRoGJCqAOT+UJShmmw6vPxCNF4hoXF8ghDRWshSMmDyiknBEGG5xvkKEMRZuJasQA)

----

```ts
type TopNavState = {
  [K in 'userId' | 'pageTitle' | 'recentFiles']: State[K]
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5AVwGdoBJAEwC5liwpQBzAbn2QAc5GIAVYMADYQadBiBZsoEJOABiwIcRH0mAbQC6rAp24BhAPbgI4JbRXjWAX1xgAnuxQ997AHJwAbukwoAvDjaqANLIoMgA5CTkFGHIAD7hOrz8QjHxYVIyYPKKYeo0XpBB6riWrEA)

----

```ts
type TopNavState = Pick<State, 'userId' | 'pageTitle' | 'recentFiles'>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5AVwGdoBJAEwC5liwpQBzAbn2QAc5GIAVYMADYQadBiBZsoEJOABiwIcRH0mAbQC6rAp24BhAPbgI4JbRXjWAX1xgAnuxQ997AHJwAbukwoAvMgAKwAgA1gA8XpAANMgA5CTkFDHIAD6xOrz8QkmpMVIyYPKKMQB8rEA)

----

```ts
interface SaveAction {
  type: 'save';
  // ...
}
interface LoadAction {
  type: 'load';
  // ...
}
type Action = SaveAction | LoadAction;
type ActionType = 'save' | 'load';  // Repeated types!
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpwG4QIILMAexGQG8AoZZMATwAcIAuZAcgGdMJmBuC5Aej7IAdCLIBfMqEixEKADIE4AE1z4ipXjXpNmAG0VLuvAcNEStKVYWIBeNByvqAPsgXLHIHheQeAKnRQ7Ng5mZBc9A25KEwAlCHo4SCUqANYAQjIgA)

----

```ts
type ActionType = Action['type'];
//   ^? type ActionType = "save" | "load"
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpwG4QIILMAexGQG8AoZZMATwAcIAuZAcgGdMJmBuC5Aej7IAdCLIBfMqEixEKADIE4AE1z4ipXjXpNmAG0VLuvAcNEStKVYWIBeNByvqAPsgXLHIHheQeAKnRQ7DwBtZgtmAF0eE0oAPQB+KgCfPGt-emQ7ACJ2LCzkFyz9ZSyyIA)

----

```ts
type ActionRecord = Pick<Action, 'type'>;
//   ^? type ActionRecord = { type: "save" | "load"; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpwG4QIILMAexGQG8AoZZMATwAcIAuZAcgGdMJmBuC5Aej7IAdCLIBfMqEixEKADIE4AE1z4ipXjXpNmAG0VLuvAcNEStKVYWIBeNByvqAPsgXLHIHheQeAShAQCKCVkOwAFYAQAawAeDwAaFgtmAD4eE0oAPQB+KjpLPGt-QODQ0jztZAAidiwq5Bcq-WUqrmQJIA)

----

```ts
interface Options {
  width: number;
  height: number;
  color: string;
  label: string;
}
interface OptionsUpdate {
  width?: number;
  height?: number;
  color?: string;
  label?: string;
}
class UIWidget {
  constructor(init: Options) { /* ... */ }
  update(options: OptionsUpdate) { /* ... */ }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIAczAPYgM7IDeAUMsgO7AAmYAFgFzIgCuAtgEbQDcpytEwAOa0wjFh268E2ADbYojPGCihBPMjLicZi5ap4BfYqEixEKDFlx4AquipxIRXpRq0A-GLaco6vgOEwTyZvSTJpOShgpRUQNV5NbWi9OMNiBE08AhsASQB1akEIMGdw62VmBDB5AApQYFE0TBx8AEoiZAB6ACpkADoB5G7O5CMyZntHCBrsZutGSxbbSch2wi7egb6hkaMjIA)

----

```ts
type OptionsUpdate = {[k in keyof Options]?: Options[k]};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIAczAPYgM7IDeAUMsgO7AAmYAFgFzIgCuAtgEbQDcpytEwAOa0wjFh268E2ADbYojPGCihBPMjLicZi5ap4BfYmACe6FBiy48AVXRU4kZAF4iAbQDWyUMg8QT2DBomDj4ALoA-IyWoXieYQY8QA)

----

```ts
type OptionsKeys = keyof Options;
//   ^? type OptionsKeys = keyof Options
//      (equivalent to "width" | "height" | "color" | "label")
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIAczAPYgM7IDeAUMsgO7AAmYAFgFzIgCuAtgEbQDcpytEwAOa0wjFh268E2ADbYojPGCihBPMjLicZi5ap4BfYmACe6FBiy48AaQgmCAXmQBre9hhpMOfDwD0fmTIAHoA-Mim5l5W+HYOyM5uJh7RPnjGZigAShB4sgBuEAA8WXDkAHwJyKXkyBAAHpAgVAQAYswgCDHI4TXIjIQA2jbIoK7unjUAuow1w1MGPJEoAMom4LSWaXFO1bkFxVvWO+X+gWRhEZnIaxtHsfa7AESUNLRPyAA+yE-8QiIfb5PaRyKCAn6abRPYjEIA)

----

```ts
// same as OptionsKeys = keyof Options, this pattern is very common and is included in the standard library as Partial
class UIWidget {
  constructor(init: Options) { /* ... */ }
  update(options: Partial<Options>) { /* ... */ }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgPIAczAPYgM7IDeAUMsgO7AAmYAFgFzIgCuAtgEbQDcpytEwAOa0wjFh268E2ADbYojPGCihBPMjLicZi5ap4BfYgk14CAVQCSAdWqCIYIlNxKozBGHkAKUMFFpMHHwASiJkAHoAKmQAOjjkSPDkIzJmdCo4SC9sQJdGAAU4KCw4GQAeDCwXAD5QwgjouJiEpKMjIA)

----

```ts
interface ShortToLong {
  q: 'search';
  n: 'numberOfResults';
}
type LongToShort = { [k in keyof ShortToLong as ShortToLong[k]]: k };
//   ^? type LongToShort = { search: "q"; numberOfResults: "n"; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoAsD2UwBVMAymIA5sgN4BQyyAjgFzIDkAzhHFAukwNzXIhGTEAFcAtgCNoAeRgAlCCxEAbMC16UAvpTABPAA4oipfBmxhkAXgrIA2gGtkoZPYi7MMNFhz5jZOCxe5r7EJA4AuuGMjpp8APRxNMgAegD8yHqGyH6m3hbW5MhsHFyMAES0ZTwC4lJQsgpKqizlIFXI2kA)

----

```ts
interface Customer {
  /** How the customer would like to be addressed. */
  title?: string;
  /** Complete name as entered in the system. */
  readonly name: string;
}

type PickTitle = Pick<Customer, 'title'>;
//   ^? type PickTitle = { title?: string; }
type PickName = Pick<Customer, 'name'>;
//   ^? type PickName = { readonly name: string; }
type ManualName = { [K in 'name']: Customer[K]; };
//   ^? type ManualName = { name: string; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/JYOwLgpgTgZghgYwgAgMIFcDOYD2BbaZAbwChlkB6AKiuQAkcB3ZMACxQS1wKmUZ3QAbACbJBwANYpcyAEYo4w4VAiZMEYQDpkVCmRbAwgiAH4AXMmxRQAcwDc+6rVT4ADscjIQcAsjiZkCHBoDWRQFnZLAE9sCDxtXX0VRRwQQSivHwgLK1sHAF8SEjAo1xQABWAECQAVQ2NkAF5kSuqAHgxsfGgAGmQAcjB6iH6APgcKCnJkAD0TFlKKqtrhpuIDI1McsGsQe2RCkrKW5YA5LLXWiQ6ubqg+-u8CMYmp8jmF46vz32aiZGSwlS6UyBG2u32h0WyAAsnAQOg4IIfig-sgANoAaTCIAGTxGAF0LJ1uNAsQS7AdXtMPkcUHCEUiUWt-vjwXkDiQgA)

----

```ts
type PartialNumber = Partial<number>;
//   ^? type PartialNumber = number
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/C4TwDgpgBACghgJ2ASzgGwHIFcC2AjCBKAXlkRXQB4A7XAhAPgG4AoAejai4D0B+KUJDJJUmOoRJRa+QiyA)

----

```ts
const INIT_OPTIONS = {
  width: 640,
  height: 480,
  color: '#00FF00',
  label: 'VGA',
};
interface Options {
  width: number;
  height: number;
  color: string;
  label: string;
}
// or
type Options = typeof INIT_OPTIONS;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/MYewdgzgLgBAkgOTgFQPoHkAKy7oQZRgF4YBvAKBhgHcBLAEygAsAuGANgBYAGAGkphMAprQDmTKG04AOPgNAAbEACc2AcgDE3bgDEd2tfyoKAhgCMhC9QDUA4gEFD5AL4BuclACeAByEx03lC04BDEMF6+IABm8EhoWDh4+O5AA)

----

```ts
function getUserInfo(userId: string) {
  // ...
  return {
    userId,
    name,
    age,
    height,
    weight,
    favoriteColor,
  };
}
// Return type inferred as { userId: string; name: string; age: number, ... }

type UserInfo = ReturnType<typeof getUserInfo>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/MYewdgzgLgBAkgOTgFQPoHkAKy7oQZRgF4YBvAKBhgHcBLAEygAsAuGANgBYAGAGkphMAprQDmTKG04AOPgNAAbEACc2AcgDE3bgDEd2tfyoKAhgCMhC9QDUA4gEFD5AL4BucgDMArmGBRa4DCiQlAAqhBCynBgHiAAFF4RUfRs0Mq0YKIAlGQCAPR5MADC6ACymABKAKL4+PLg0DBgJgC2QsQwagBCIGZq7lSgkLAmwR0AjABMAzBDjcJiEh0yM3Ow1CLisCQA7NyrDbAeJgBuKrRQQkUgSsodamYKXkL9+YVVCAAiAsohXspgXJUKiJSJwehGYHNNqQqijISwwSbCSIjaLKCI45ndKXa63SFuFzkAowCp-AEwKAATwADu0Mh5Ir96DATBAyDBQclUlB0plXE1WkIeXzRAL4WwwF4WhZlLwYAA6JUwZzkcjUukwcJgmIgDpkqD-MDIWlCAA8GqEIA8QRC2qiuoAfO4gA)

----

```ts
interface Product {
  id: number;
  name: string;
  priceDollars: number;
}
interface Customer {
  id: number;
  name: string;
  address: string;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgApQPYBMCuCzIDeAUMssFgFzIg4C2ARtANyk1x0TUDOYUoAc1ZkADvyQARDABtpcKN2q1GLYgF9ioSLEQoAwjl4ZOUImwpL6TKMPacefQbbhYsUCN0XJe-EEPXEQA)

----

```ts
// Don't do this!
// this is because while the id and name properties happen to have the same name and type, they're not referring to teh same thing. 
// In this case, factoring out the common base interface is a premature abstraction which may make it harder for the 2 types to evolve independently in the future. (as Product and Customer is likely evolve differently)
// a good rule of thumb is that if it's hard to name a type ( or a function, then it may not be a useful abstraction. In this case, NamedAndIdentified) just describes the structure of the type, not what it is. The Vertebrate type from before, on the other hand, is meaningful on its own. Remember, "duplication is far cheaper than wrong abstraction"
interface NamedAndIdentified {
  id: number;
  name: string;
}
interface Product extends NamedAndIdentified {
  priceDollars: number;
}
interface Customer extends NamedAndIdentified {
  address: string;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBEHsDsHIBdQBNKngCwJYGcCEAoTaeAUwCcAzAQwGMTQA5KgWxKQEFokBJJE4zBUxtQAb3yhQmJAC5Q0AK7MARuQDcE+SxJzs8MkQDmGgL6Fi5anVAAFMpCQKaiEgA9SXbI20cuvfvCCwkhimgAOBnRQADbRVGTYcooq6vhmRKSUtPQAwgp6kKxkoG4eSF5MrL48fAJCIuKSVEhIZCTYiaB6BtDGafhAA)


# Prefer More Precise Alternatives to Index Signatures

## Things to Remember

- Understand the drawbacks of index signatures: much like `any`, they erode type safety and reduce the value of language services.
- Prefer more precise types to index signatures when possible: ++interface++s, `Map`, ++Record++s, mapped types, or index signatures with a constrained key space.



## Code Samples

```ts
const rocket = {
  name: 'Falcon 9',
  variant: 'Block 5',
  thrust: '7,607 kN',
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBATiYBrAprAvDA3gKBjMAQwFsUAuGAcgDFCAbUMGATkoBo8YA3QuAS0JgoFSgCE6iJDACs7TlAAWcAK7QRAdjYA2AAzqYSAHJyAvgG4cQA)

----

```ts
type Rocket = {[property: string]: string};
const rocket: Rocket = {
  name: 'Falcon 9',
  variant: 'v1.0',
  thrust: '4,940 kN',
};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBASg9gYwNYWFAvFA3gbTAJzkn1AC4oBnYfASwDsBzAXXKtsYF8BuAKATjpUohZKnLxRaTFh5QodAIYBbCOQDkAMQUAbfnSgBONQBpZUAG4LaCusHXmAjADoADCbPAAFvgCuVdQAsxgYBLlBIAHLu3HIA9LFQAPIA0jxAA)

----

```ts
interface Rocket {
  name: string;
  variant: string;
  thrust_kN: number;
}
const falconHeavy: Rocket = {
  name: 'Falcon Heavy',
  variant: 'v1',
  thrust_kN: 15200,
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYgA)

----

```ts
function parseCSV(input: string): {[columnName: string]: string}[] {
  const lines = input.split('\n');
  const [headerLine, ...rows] = lines;
  const headers = headerLine.split(',');
  return rows.map(rowStr => {
    const row: {[columnName: string]: string} = {};
    rowStr.split(',').forEach((cell, i) => {
      row[headers[i]] = cell;
    });
    return row;
  });
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQhAA)

----

```ts
interface ProductRow {
  productId: string;
  name: string;
  price: string;
}

declare let csvData: string;
const products = parseCSV(csvData) as unknown[] as ProductRow[];
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZsIA)

----

```ts
function parseCSVMap(input: string): Map<string, string>[] {
  const lines = input.split('\n');
  const [headerLine, ...rows] = lines;
  const headers = headerLine.split(',');
  return rows.map(rowStr => {
    const row = new Map<string, string>();
    rowStr.split(',').forEach((cell, i) => {
      row.set(headers[i], cell);
    });
    return row;
  });
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tCAA)

----

```ts
const rockets = parseCSVMap(csvData);
const superHeavy = rockets[2];
const thrust_kN = superHeavy.get('thrust_kN');  // 74,500
//    ^? const thrust_kN: string | undefined
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tDIzAcDALtN1qRpd33Kta3rOAXRbWgJEqaBAmsPYAXsHTBiyWZm1ZZAxEkGR5D2SzrKgWyrEOJhxI8TzklSXESAAemi5AAHYABYQgyPJCFi40AD0AH4WRfDykm8tI72QAAfZASneGBtleQggA)

----

```ts
function parseRocket(map: Map<string, string>): Rocket {
  const name = map.get('name');
  const variant = map.get('variant');
  const thrust_kN = Number(map.get('thrust_kN'));
  if (!name || !variant || isNaN(thrust_kN)) {
    throw new Error(`Invalid rocket: ${map}`);
  }
  return {name, variant, thrust_kN};
}
const rockets = parseCSVMap(csvData).map(parseRocket);
//    ^? const rockets: Rocket[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tGKUpyiqHs7Bwc4KUqM9KRoxZ6MWel+jQTB9KZFt0z2QzDiYcSPHTf9n30CJgF4PBnCclzsW83yPJZF9kDESQZHkPY5GUNQoBaALXMi5JUluZjgBgZAWgAQgcgAfArkFy4LwGQIr9loCY5BaVLorkXoDWEiLxCBUgIGjFUoABRKAAMExALgtleE17GPAASfBDI0PrmK0LClI9fB0x+MqwB+eqUnkcUtDImzcC7TdakaXd9yrWt6zgXp8KpY6ID03AXQAeme40AD0AH4wv0AFxtoWwDrAFZCCAA)

----

```ts
interface Row1 { [column: string]: number }  // Too broad
interface Row2 { a: number; b?: number; c?: number; d?: number }  // Better
type Row3 =
    | { a: number; }
    | { a: number; b: number; }
    | { a: number; b: number; c: number;  }
    | { a: number; b: number; c: number; d: number };  // Also better
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tH9aB4CQNAgViAhkE5bkQHzQUlFUaBkBFZAAHobOQAAVdB0GQFQAXhP1wC0oNdMBLIDMbUhlDUKAWFcgB+RRgvUaFIqCizQuQV44vMkKrJIOzkAAIVwANCDAKxKhQKMAGYnFdAAfAKooSsKtGNKr8BnGqQrClQWpi+rmUa5r4ta1yOsShBBrCqzKuqvqYvayahpGpLBqs0bMoAQUMWgXLUMA8qAA)

----

```ts
type Vec3D = Record<'x' | 'y' | 'z', number>;
//   ^? type Vec3D = {
//        x: number;
//        y: number;
//        z: number;
//      }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tDAKxKhQJoIAQABmGs9lQPTlVeC8PAADw8ZAAB9omCOzogAL1CUhlDUKB6TYAB6HzmQAPQAfmQTTtOQXSDKM5wiD841jUsxQPPUQg4vikgbHc1QUrS9LnKS7KoF8-z4q0IA)

----

```ts
declare function renderAButton(props: ButtonProps): void;
interface ButtonProps {
  title: string;
  onClick: () => void;
}

renderAButton({
  title: 'Roll the dice',
  onClick: () => alert(1 + Math.floor(6 * Math.random())),
  theme: 'Solarized',
// ~~~~ Object literal may only specify known properties…
});
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/CYUwxgNghgTiAEAzArgOzAFwJYHtXzlVBgEEAhZDDPACgAcYc6BnALngqrwAVGWBKdgDccWYAG4AUFlQYQMRFDAJO1VLybN4Ab0nx42DBBDtmGGDIDmU-XgDCELGADW7Gv3gBeAHzwRYqQBfSUlCYnJKNRpdfUNjdgByACUcCAgDAAsEYCcQBIAaPXh7Rxc3Dx94KGMYDBoARngAangAWSgMDIA6RAgcHBgaADZ4ACo2ju6YKCIcAFt3fn5C2Ky5k3gEgGVU2CwALxBgAskAelP4AD9ry-gAeQAjACtwDHhHOWn0uagAT2LUBB-sw6OAsIh-s5UDgAO74BhMeTYEDMQBkBJJAvwpEA)

----

```ts
interface ButtonProps {
  title: string;
  onClick: () => void;
  [otherProps: string]: unknown;
}

renderAButton({
  title: 'Roll the dice',
  onClick: () => alert(1 + Math.floor(20 * Math.random())),
  theme: 'Solarized',  // ok
});
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/CYUwxgNghgTiAEAzArgOzAFwJYHtXzlVBgEEAhZDDPACgAcYc6BnALngqrwAVGWBKdgDccWYAG4AUFlQYQMRFDAJO1VLybN4Ab0nx42DBBDtmGGDIDmU-XgDCELGADW7Gv3gBeAHzwRYm3gAbRwMAAt5DRZTcysAXXY0Z1QcAHdUKQBfSUlCYnJKNRpdfUNjdgByACUcCAgDCPhgJxAKgBo9eHtHFzcPH3goYxgMGgBGeABqeABZKHCAOkQIHBwYGgAmAAZ4ACpZ+bCFmCgiHABbd35+DtKI85N4CoBlWtgsAC8QYHb9AHo-l1nJJMvwpEA)


# Avoid Numeric Index Signatures

## Things to Remember

- Understand that arrays are objects, so their keys are strings, not numbers. `number` as an index signature is a purely TypeScript construct designed to help catch bugs.
- Prefer `Array`, tuple, `ArrayLike`, or `Iterable` types to using `number` in an index signature yourself.
## Code Samples

```ts
interface Array<T> {
  // ...
  [n: number]: T;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgIJSnAngHgCoB8yA3gFDLID0lyAdPecgNogBcyIArgLYBG0AXXZ4A3KQC+pIA)

----

```ts
const xs = [1, 2, 3];
const x0 = xs[0];  // OK
const x1 = xs['1'];  // stringified numeric constants are also OK

const inputEl = document.getElementsByTagName('input')[0];
const xN = xs[inputEl.value];
//            ~~~~~~~~~~~~~ Index expression is not of type 'number'.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKFEljgAZl4JVqSYYB6VmAeQGlzxp46OglQBydKOZsO0AE4BLMAHN5AM3kBTACYwwAVwC2GhcBgVoAQzBREF2RpgWANhBBdefSjEUAHPVABRJzotEGBDDWsAOiUNQKcNI2sIACEATwAVCyUAOQsjAApRX39RAEpGEk8BOBzhBhL4qIA3Zz0NKvYWbp7ugD8BwaHBmABJMC0NOBgpn3sICHlwb0QwEFgQVRgoNJ8HUX0DACNjUSjSIA)

----

```ts
const keys = Object.keys(xs);
//    ^? const keys: string[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKFElgGsBTAT0RQHkAjAKxuCgDpaGAKBAEoyAelExJMAHoB+GBWgw+EAFwAC6ACcAlmADmqQqSA)

----

```ts
function checkedAccess<T>(xs: ArrayLike<T>, i: number): T {
  if (i >= 0 && i < xs.length) {
    return xs[i];
  }
  throw new Error(`Attempt to access ${i} which is past end of array.`)
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKADMBXMYKAS3BmAAsBTYAa1YBMBBYYKwgQAPABUAfAAoEALhi8ATooCGATwAydLuInY68sJQC2AI1aKAlPLEwA3qRgw65GFLowJKAAwwAZH7OMCLwEAB0ADasYADmUMyW9o5OMIqsUJSKYKGodCTJAL7J8YogAO4wYKwVAKLKIIpSAAa8UFCsxgAOsFAgMCoCQogAJHZ0BTBlzHQszoidKtAw0dwwIK4qyuphTZakRUA)

----

```ts
const tupleLike: ArrayLike<string> = {
  '0': 'A',
  '1': 'B',
  length: 2,
};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKFEligFcAHAGwFMAZASwGtGAuGAQQCd+AQwCebTgB5o-VmADmAPmQwA3qRgwA5AAZNPTb02Z1W9Hq0AhIyabyoACx55SAX2IaA9B5gB5ANKkQA)


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
