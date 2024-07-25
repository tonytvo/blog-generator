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
// if several functions share the same type signature, you can factor out a named type for this signature
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
// this is because while the id and name properties happen to have the same name and type, they're not referring to the same thing. 
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
type Rocket = {[property: string]: string};
// this is index signatures, it specifies 3 things:
// 1) the name for the keys
// 2) a type for the key
// 3) a type for the values

// while the code does type check, it has few downsides:
// 1) it allows any keys, including incorrect ones. Had you written Name instead of name, it would have still been a valid Rocket type
// 2) it doesn't require any specific keys to be present, {} is also a valid Rocket
// 3) it cannot have distinct types for different keys, we might want thrust to be a number rather than a string.
// 4) as you're typing name: there's no autocomplete because the key could be anything
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
// historically, index signature were the best way to model truly dynamic data, such as parsing CSV or JSON
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
const rockets = parseCSVMap(csvData);
const superHeavy = rockets[2];
const thrust_kN = superHeavy.get('thrust_kN');  // 74,500
//    ^? const thrust_kN: string | undefined
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoHsEGsJmQbwChlkQ4BbCALmQGcwpQBzAbmOQDc5G5wb7GIVuzAALKAFd6AfSwA5GiAnkARtDYBfQgnQh6yeABsdIABIQ4HAJ40M2XMgC8BdmUo0A5ADE4x3cnNLKw8AGnYuHj5kDw4ARlCRcSkwWQVkWIBWACYABhywjTYYCRAEMGB-AAduWggAYQBlADUAClBKiTB+BmYAShp8AG0dQ2UQOQpqOh6hAF1uwSYNQdmXEhN9Q1AIWidkds6AOlpKrbAWjwAdEA9etnXdfUHRCwATaAAZbZDkQ7+odAAd1oq2cWxAO3uyA2eBecHeUF2zjhCK+EOOp2A51CtyhUFwEigIGQAOBh3IcEqLVJDQYTgAfGsSNDHnhSQNhuhRuRxpMFsx5tNFho9vhCuwSDSGBizhcQrdDjB0FAAKKIUQtFpIQyGH7AXoMpnMklA55vaC0QbAWag6EQHVQkgaO4SkkEokmwFQ52aQigSCwRAoAAKANeEjKGEBTMqYYjYAAkq9+UIoW4pgJmFDY8AkCnhFpCO8EIZuChDA4ELQOAAROBgOD5tgw5Cx9DhspI1s1erNLXVusNg1wXYlLAgIEgFbIEfIUPt+NRlZFEplCrE6qI3tNACylLaIA6XSFfRoe8qAB5M0IftemPTp0QHno8OCdnsDmAZViLtdcewWzNeFPm+X5-iBEE9jfWgoRbFELT2eCoDRCBv2xeUXUld1iVJWhyX3KUoENJ9mRbUk9ghaNzyvGYmFvWj6RaTDmUItC5QVJVVXVTVtV1fYDUcRkSONUljlwFokMta0fl45inTkt0wEJHCgW9F0tDIzAcDALtN1qRpd33Kta3rOAXRbWgJEqaBAmsPYAXsHTBiyWZm1ZZAxEkGR5D2SzrKgWyrEOJhxI8TzklSXESAAemi5AAHYABYQgyPJCFi40AD0AH4WRfDykm8tI72QAAfZASneGBtleQggA)

----

```ts
// if you want to get an object type out of a Map, you'll need to write some parsing code
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
// if your type has a limited set of possible fields, don't model this with an index signature, if you know your data will have keys like A, B, C, D, but you don't know how many of them there will be, you could model the type either with optional fields or a union.
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
// Record is a built-in wrapper around a mapped type
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
// you can use an index type of disable excess property checking, for example, you might define a few known properties on a ButtonProps type but still want to allow it to have any others.
// you can constraint these additional properties to match a certain pattern. For example, some web components allow arbitrary properties but only if they start with "data-", you can model this using an index signature and a template literal type
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
// in particular, numbers cannot be used as keys. If you try to use a number as a property name, the javascript runtime will convert it to a string
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKFEljgAZl4JVqSYYB6VmAeQGlzxp46OglQBydKOZsO0AE4BLMAHN5AM3kBTACYwwAVwC2GhcBgVoAQzBREF2RpgWANhBBdefSjEUAHPVABRJzotEGBDDWsAOiUNQKcNI2sIACEATwAVCyUAOQsjAApRX39RAEpGEk8BOBzhBhL4qIA3Zz0NKvYWbp7ugD8BwaHBmABJMC0NOBgpn3sICHlwb0QwEFgQVRgoNJ8HUX0DACNjUSjSIA)

----

```ts
x = [1, 2, 3]
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
// a general rule, there's not much reason to use number as the index signature of a type. if you want to specify something that will be indexed using numbers, you probably want to use an ArrayLike or tuple type instead.
const tupleLike: ArrayLike<string> = {
  '0': 'A',
  '1': 'B',
  length: 2,
};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBAHhGBeGBtAjAGhgJmwZgF0BuAKFEligFcAHAGwFMAZASwGtGAuGAQQCd+AQwCebTgB5o-VmADmAPmQwA3qRgwA5AAZNPTb02Z1W9Hq0AhIyabyoACx55SAX2IaA9B5gB5ANKkQA)


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

# Use Different Variables for Different Types

## Things to Remember

- While a variable's value can change, its type generally does not.
  - the one common way a type can change is to narrow
- To avoid confusion, both for human readers and for the type checker, avoid reusing variables for differently typed values.

## Code Samples

```ts
let productId = "12-34-56";
fetchProduct(productId);

productId = 123456;
// ~~~~~~ Type 'number' is not assignable to type 'string'
fetchProductBySerialNumber(productId);
//                         ~~~~~~~~~
// Argument of type 'string' is not assignable to parameter of type 'number'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABMAplCALACgJzgExGgAoZ8AuRAZyhxjAHMBKRAbwF8AoUSWBZNJlwEiUAEIBPAMoo6AQwA2AORABbAEazSFRGDWacLDpwVpEABzyFoASXyIAvIgBEARgBMAWgDMAFk8ArABszgDc3ILYVqLEliK2+EzhnHHWUHaOiB5+weEA9HmIAH4lpYgAKhLmKIgA5HoasrWIMFS6cFCIclRUMAxgcuqmiFBwI1U1tTR0jLUR6FHx4tKyMIoqjTix0QlJnAWIh0fHJ6fHpRcl+4UAgjgMaihgnXDA49V10-QMza3tnd1ev1BsNRhY5Dg5Ko0LJEK93pMGgY5kA)

----

```ts
let productId: string | number = "12-34-56";
fetchProduct(productId);

productId = 123456;  // OK
fetchProductBySerialNumber(productId);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABMAplCALACgJzgExGgAoZ8AuRAZyhxjAHMBKRAbwF8AoUSWBZNJlwEiUAEIBPAMoo6AQwA2AORABbAEazSFRGDWacLDpwVpEABzyFoASR006jRAB9d+2YgC8iAEQBGACYAWgBmABYggFYANh8Abm5BbCtRYksRW3wmBM506yg7L0RA8Ji4xEQAekrEAHkAaUT0ZIzxaVkYRRUNLTzRO2yK6rrGoA)

----

```ts
// better solution to union type is to introduce different variables
// - it disentangles 2 unrelated concepts (ID and serial number)
// - it allows you to use more specific variable names
// - it improves type inferences, no type annotation needed
// - it results in simpler types (string and number literals, rather than string | number)
// - it let you declare variable const rather than let. This make it easier for hte type checker and people to reason about.
const productId = "12-34-56";
fetchProduct(productId);

const serial = 123456;  // OK
fetchProductBySerialNumber(serial);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABMAplCALACgJzgExGgAoZ8AuRAZyhxjAHMBKRAbwF8AoUSWBZNJlwEiUAEIBPAMoo6AQwA2AORABbAEazSFRGDWacLDpwgIaiAA55C0AJL5EAXkQAiAIwAmALQBmACxeAKwAbC4A3NyC2NaixFYidvhMESZmUNSyMIpOiJ7+IWGIiAD0xYgA8gDSkejRCeLSmYoqGlpUTQrJRaUV1UA)

----

```ts
const productId = "12-34-56";
fetchProduct(productId);

{
  const productId = 123456;  // OK
  fetchProductBySerialNumber(productId);  // OK
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABMAplCALACgJzgExGgAoZ8AuRAZyhxjAHMBKRAbwF8AoUSWBZNJlwEiUAEIBPAMoo6AQwA2AORABbAEazSFRGDWacLDpwgIaiAA55C0AJL5EAXkQAiAIwAmALQBmACxeAKwAbC4A3NyC2NaixFYidvhMEZysnIiIpmDm8TZQ9k6Inv4hYRkA9OWIAPIA0ukC6NEJ4tKyMIoqGlq5ovbJFVV1nFxAA)


# Understand How a Variable Gets Its Type

## Things to Remember

- Understand how TypeScript infers a type from a literal by widening it.
- widening process is when typescript needs to decide on a set of possible values, from a single value that you specified.
- Familiarize yourself with the ways you can affect this behavior: `const`, type annotations, context, helper functions, `as const`, and `satisfies`.

## Code Samples

```ts
interface Vector3 { x: number; y: number; z: number; }
function getComponent(vector: Vector3, axis: 'x' | 'y' | 'z') {
  return vector[axis];
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREgA)

----

```ts
// the general fule for primitive value assigned with let is that they expand to their "base type"; x expands to string, 39 expands to number, true expands to boolean, and so on (null and undefined are handled differently)
let x = 'x';
let vec = {x: 10, y: 20, z: 30};
getComponent(vec, x);
//                ~ Argument of type 'string' is not assignable
//                  to parameter of type '"x" | "y" | "z"'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREAGwUSZABedydk9LBkKOzCMmQARgAGC1ZkACZq7nJcSsFk+SUVdRBNMF0MC2I-ZIB6EeCJyanggD9kAEEoWRpe5CwYZDBmVRR7GzAoUFlnWwosQrgbG2BZEDhadOEx6Zep7GRVOCg4agVoNY2Wx27gARMQQa5kCDmBC3CCuCD7MIgA)

----

```ts
// if you declare a variable with const instead of let, it gets a narrower type.
const x = 'x';
//    ^? const x: "x"
let vec = {x: 10, y: 20, z: 30};
getComponent(vec, x);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswEmQAXncnZIB6AuDggD0AfmQ0kAyScgAiYnrhABsFZCicwjJkAEYABgtWZAAmQe5yXH7BZPklFXUQTTBdDAtiPyZkIuQAeQBpYSA)

----

```ts
// in the case of objects, TypeScript infers what it calls the "best common types", It determines this by treating each property as through it was assigned with let. so the type of obj.x comes out as number, this lets you assign obj.x to different number but not to a string. And it prevents you from adding other properties via direct assignment.
const obj = {
  x: 1,
};
obj.x = 3;  // OK
obj.x = '3';
//  ~ Type 'string' is not assignable to type 'number'
obj.y = 4;
//  ~ Property 'y' does not exist on type '{ x: number; }'
obj.z = 5;
//  ~ Property 'z' does not exist on type '{ x: number; }'
obj.name = 'Pythagoras';
//  ~~~~ Property 'name' does not exist on type '{ x: number; }'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswZCxaACtkAF5A4LJkAEYzFOTsnIA6YgLkXCZkAHoW5AB5AGlharqG+1x7ZLbggD9kABVmVRR7DKhQWWdbCixMuBsbYFkQOFoAGxRsZDAZufZ+e17cmuYGgBYR9uQJgAUoLFmoM-dPZAAJlgIDY1pkINYMlkZGdZu4iCVLpxBNc+lwGgBWZ7jZAfL7QX4+ZxAkFg5AQ2yZaSnc7wki8DgCZAom61PbUFCFexvZhgAAWcFkOE2w2Eo1eY0luM+30J7IgxOBoJA63JkKpMNp9gRDP4QmuQA)

----

```ts
// override default typescript behaviors
const obj: { x: string | number } = { x: 1 };
//    ^? const obj: { x: string | number; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswZCxaACtyIjJkDKhQWVcKPmhkQWQAXkIScgBGauSAejbg4IA9AH5kNJAMrNz8xqKwEpAyt3Z+IWEgA)

----

```ts
const obj1 = { x: 1, y: 2 };
//    ^? const obj1: { x: number; y: number; }

const obj2 = { x: 1 as const, y: 2 };
//    ^? const obj2: { x: 1; y: number; }

const obj3 = { x: 1, y: 2 } as const;
//    ^? const obj3: { readonly x: 1; readonly y: 2; }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswZCxaACsARmQAXkIScjyLVmQAJmRBZIB6euDggD0AfmQ0kAys3LzyIjIKPk5K9n4hYWEunuycmuLBsssbTvSwCvIauuFG5uR2te7MuaqB0uQ8pjGRgVqpmZPc-EWL8pYt2pWjjIam5sOj16OVw51CcAAJtIADbMN5McFQkCwj7VSZAA)

----

```ts
// while type assertion are best avoided, a const assertion doesn't compromise type safety and is always OK
const arr1 = [1, 2, 3];
//    ^? const arr1: number[]
const arr2 = [1, 2, 3] as const;
//    ^? const arr2: readonly [1, 2, 3]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswSygoAEZkAF5kGJyLACYLXCThAHpq4OCAPQB+ZDSQDKzc3g5YhOE2jrhs0oKikuRy5ErLG1b0sGTa+uRmufbMoahS8lC4ABNpABtmMbKKvqA)

----

```ts
function tuple<T extends unknown[]>(...elements: T) { return elements; }

const arr3 = tuple(1, 2, 3);
//    ^? const arr3: [number, number, number]
const mix = tuple(4, 'five', true);
//    ^? const mix: [number, string, boolean]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYRExCTApGTBKVQAbCAAeABVkCGJIEAATG2RxAGsQLAB3EBiEgD4tADoeiHzqTTA7ZCKAolDsiNL+wZshYWEEaRswSyg8ZABeZGy8iC0ARgsAJgtcP2SAekvg4IA9AH5kJZAVtbxyGPZ+C2-oX740ASi2Wq2owGIWx2OXyWgALBZ7DBgHp7BYwFBKBALsJrrdkI9nqDkOCyMgvoCoBYVlBQLILLQsFh8nAQMCgA)

----

```ts
// like const, Object.freeze has introduced some readonly modifiers into the the inferred types 
// unlike the const assertion, the "freeze" will be enforced by your javascript runtime, but it's shallow freeze/readonly, whereas const assertion is deep.
const frozenArray = Object.freeze([1, 2, 3]);
//    ^? const frozenArray: readonly number[]
const frozenObj = Object.freeze({x: 1, y: 2});
//    ^? const frozenObj: Readonly<{ x: 1; y: 2; }>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREEaRswZBgoLC5NAEEoKDhmZABeZAB5WgArfQA6bIgIPK0YgEYLACYLXAS-ZIB6QeDggD0AfmQ0kAysnLyQQuLWEIg4ABNpABtS9n4YhOEZuezczWqa8qrahqaWiC0CMmROlnIuwQHhYdHkSem6UyZ0Wl3IACV1lsQLsADxEF7tJirLpCAB8wiAA)

----

```ts
type Point = [number, number];
const capitals1 = { ny: [-73.7562, 42.6526], ca: [-121.4944, 38.5816] };
//    ^? const capitals1: { ny: number[]; ca: number[]; }

const capitals2 = {
  ny: [-73.7562, 42.6526], ca: [-121.4944, 38.5816]
} satisfies Record<string, Point>;
capitals2
// ^? const capitals2: { ny: [number, number]; ca: [number, number]; }
// satisfies prevent the values from being widened beyond the Point type
// this is an improvement over a const assertion because it will report the error where you define the object, rather than where you use it.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREwZlUUAAUsUDBkAF5kGPZ+CxLoJOEEaRs8hDhVYDA4ABsbAEYCwgpWIoBaAHZcADoBgFYANgAmCwAWKeGJsamJhIt68hi+9qn24dmATlnZi1wADmGxs-bV5EFkgHoH4OCAPQB+ZGqQWq+GptaHXIRBAvXKsSSf14HAhQmEVRqdX+zTaUy6BCCPU2gxG42mcwWSxWayh-R2e0Ox1OFyuNwSKWQNjgYFsMGAEBsyAAShgcAATAA8tSgoFkFmyuQAfMl6o0UTYpsInsgPl9EX85YCpsCsUVwWU+BUmBs9YaoAaYZCREA)

----

```ts
const capitals3: Record<string, Point> = capitals2;
capitals3.pr;  // undefined at runtime
//        ^? Point
capitals2.pr;
//        ~~ Property 'pr' does not exist on type '{ ny: ...; ca: ...; }'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREwZlUUAAUsUDBkAF5kGPZ+CxLoJOEEaRs8hDhVYDA4ABsbAEYCwgpWIoBaAHZcADoBgFYANgAmCwAWKeGJsamJhIt68hi+9qn24dmATlnZi1wADmGxs-bV5EFkgHoH4OCAPQB+ZGqQWq+GptaHXIRBAvXKsSSf14HAhQmEVRqdX+zTaUy6BCCPU2gxG42mcwWSxWayh-R2e0Ox1OFyuNwSKWQNjgYFsMGAEBsyAAShgcAATAA8tSgoFkFmyuQAfMl6o0UTYpsInsgPl9EX85YCpsCsUVwWU+BUmBs9YaoAaYZCRN9frKAW1cOQedUoILhaLxTlwJKunb5VMZcjASNVAJgsrxHyIGyQBA+ZY8lBxCzqBAlc8XpnVRLwFUg6jhqHHhnM8EAH5l5CZKBYDJQNLuUPOPlYDkULB5CDWX7SZBpDLuEG9YYj41wcgj4ZCezCIA)

----

```ts
const capitalsBad = {
    ny: [-73.7562, 42.6526, 148],
//  ~~ Type '[number, number, number]' is not assignable to type 'Point'.
    ca: [-121.4944, 38.5816, 26],
//  ~~ Type '[number, number, number]' is not assignable to type 'Point'.
} satisfies Record<string, Point>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGoQWA9lAzMgb2QA8AuZEAVwFsAjaAbmQE9yq7HkAvNm+qJgF8AUDEohMwLCGQBzCGADCWagAdpEcAAoAbhmxRy6TDlwAaZHGLAAzuQDkxe8gA+ye82dv7XewEpCYWRkKAVKKBk9EygAbStbAF0GYREwZlUUAAUsUDBkAF5kGPZ+CxLoJOEEaRs8hDhVYDA4ABsbAEYCwgpWIoBaAHZcADoBgFYANgAmCwAWKeGJsamJhIt68hi+9qn24dmATlnZi1wADmGxs-bV5EFkgHoH4OCAPQB+ZGqQWq+GptaHXIRBAvXKsSSf14HAhQmEVRqdX+zTaUy6BCCPU2gxG42mcwWSxWayh-R2e0Ox1OFyuNwSKWQNjgYFsMGAEBsyAAShgcAATAA8tSgoFkFmyuQAfMl6o0UTYpsInsgPl9EX85YCpsCsUVwWU+BUmBs9YaoAaYZCRN9frKAW0AEJwPnozHBUHYoajSYzZDzRbLCYWdqzM5rJXPZAAPyjyAAKukUPZimaLaUKGaEs5bBQsHk4DYbMBZCA4LQWihsMg0hl3BLwPZhm7SVtyfsjidkOdLtcg8hiWYI8EY-HE+4UzC09Ap1As8gcyA85ZC8XS+XK1hq2P7PWwI2GUyWTY2RzubyoILhaLxTlwNLhEA)


# Create Objects All at Once

## Things to Remember

- Prefer to build objects all at once rather than piecemeal.
- Use multiple objects and object spread syntax (`{...a, ...b}`) to add properties in a type-safe way.
- Know how to conditionally add properties to an object.

## Code Samples

```ts
const pt: Point = {
  x: 3,
  y: 4,
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgAoHtRmQb2QDwC5kQBXAWwCNoBuZAT2LKtuQF8AoBdEAZ2wAOYYhizIAvLg7ICxAMwAaaQ2IAWJWxocgA)

----

```ts
// if you need to build larger object from smaller one, avoid doing it in smaller steps
const pt = {x: 3, y: 4};
const id = {name: 'Pythagoras'};
const namedPoint = {};
Object.assign(namedPoint, pt, id);
namedPoint.name;
// ~~~~ Property 'name' does not exist on type '{}'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgAoHtRmQb2QDwC5kQBXAWwCNoBuZAT2LKtuQF8AoBdEAZ2wAO2ALy4iyAMwAaBsQAsbGlx79kwACbJROEHHIRiAclT0wACzgBzdFDi9Di5X2y796jFi25HAeUoArCAQwADo7XmBLEAAKVwh3THAZIRkNAEolOISsELilZALCgoB6YuQAP0rytCh0AWgwemRDOMNkdXQIXhJ0bAh8YFUeZEb65pw2Qw4gA)

----

```ts
// you can build the larger object all at once using object spread syntax
const namedPoint = {...pt, ...id};
//    ^? const namedPoint: { name: string; x: number; y: number; }
namedPoint.name;  // OK
//         ^? (property) name: string
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgAoHtRmQb2QDwC5kQBXAWwCNoBuZAT2LKtuQF8AoBdEAZ2wAO2ALy4iyAMwAaBsQAsbGlx79kwACbJROEHHIRiAclT0wACzgBzdFDi9Di5X2y796jFi24AdL6Ezfbw1HAHoQ5AjkAD0AfmRuZxI9CHdMcGI8VwNkfihQSzpxZmooOkYSChK6TizUrG8sumQw5AB5AGkOFsie6LiACgEodAFoMHoASiT9Ylz8jiA)

----

```ts
// you can also use object spread syntax to build up objects field by field in a type-safe way. The key is to use a new variable on every update, so that each gets new type
const pt0 = {};
const pt1 = {...pt0, x: 3};
const pt: Point = {...pt1, y: 4};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgAoHtRmQb2QDwC5kQBXAWwCNoBuZAT2LKtuQF8AoBdEAZ2wAOYAAzIAvLjY0uPfsiEBGcbgB0aocIA0BYgGYpMvoLDEMWZTjUrF2xsgAsU5MgD0L5AHkA0hyA)

----

```ts
declare let hasMiddle: boolean;
const firstLast = {first: 'Harry', last: 'Truman'};
const president = {...firstLast, ...(hasMiddle ? {middle: 'S'} : {})};
//    ^? const president: {
//         middle?: string;
//         first: string;
//         last: string;
//       }
// or: const president = {...firstLast, ...(hasMiddle && {middle: 'S'})};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/CYUwxgNghgTiAEEQBd4AsoGcCyBLYwSAXPAEYD25SUAdgNwBQY5NmqAZrjGwDJaoBeeAG9O3ZCQDkACVgwAnpIA0iflIAqMAK4BbWpIC+jZq1QAHOJnwgagkQDpHY3vxWP7ACgw58hBAH4RHV9ieEkAZUN4EmEDAEojBgB6JPg0+AA9QJM2eAsQK1BbGOTU9PL4YIIkfxI2GFwaAHNGFIry5wl4esaW0vb06DY65Abm1rKKg37yGBIc80trW3ghYXdOvjY3Ry8sPGqEADIjoJCQKUj4xKA)

----

```ts
// you can use spread syntax to add multiple fields conditionally
declare let hasDates: boolean;
const nameTitle = {name: 'Khufu', title: 'Pharaoh'};
const pharaoh = { ...nameTitle, ...(hasDates && {start: -2589, end: -2566})};
//    ^? const pharaoh: {
//         start?: number;
//         end?: number;
//         name: string;
//         title: string;
//       }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&exactOptionalPropertyTypes=true#code/CYUwxgNghgTiAEEQBd4AsoGcAiVkkwC54AjAezKSgDsBuAKDDOs1WqgFsQAVAS2STwAvPADe7LsQDkAaTQBXAGbypAGnjJ+SaQAUMMKGTRSAvgyYtUAB32G0wsfAB0LiTy0h1LpwAoMOPAJ4ADJgsVZYZGIAWgAmAFYADgBOdRBqYBiEgDZskwBKM3oAemL4cvgAPQB+eAtWeBtYO2JRErKKzvgImGRq4mp5DhIQGAZSrs704H74QeHR8Y7Juc4QYlYYXmoAcyWV8s0Bde7kLd39yZN6IA)


# Understand Type Narrowing

## Things to Remember

- Understand how TypeScript narrows types based on conditionals and other types of control flow.
- Use tagged/discriminated unions and user-defined type guards to help the process of narrowing.
- Think about whether code can be refactored to let TypeScript follow along more easily.


## Code Samples

```ts
const elem = document.getElementById('what-time-is-it');
//in TypeScript, a symbol has a type at a location
//    ^? const elem: HTMLElement | null
if (elem) {
  elem.innerHTML = 'Party Time'.blink();
  // ^? const elem: HTMLElement
} else {
  elem
  // ^? const elem: null
  alert('No element #what-time-is-it');
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBApgGzgWxgXhgExMArsuMKAOgHM4oBRJAogIQE8BJTACgHIB3ACwEMoAtFACWBAcIjio7AJQBuAFAB6JTDUwAegH4YoSLEQoAXDAASAFQCyAGWopCsAD4wwuBAgXCAZjFaHkMjAA3gpq-sTCYGBwAE4WNugw7AAKvDFQDDDmonDsxABGCJEA1qzyoTAqmjp60PA0JvG2NA4KAL71EHDBFf4VVdq64HX+Jq7uFbxI6RwAciD19kQwAMQ8-EI54pLC0uVtCkA)

----

```ts
const elem = document.getElementById('what-time-is-it');
//    ^? const elem: HTMLElement | null
if (!elem) throw new Error('Unable to find #what-time-is-it');
elem.innerHTML = 'Party Time'.blink();
// ^? const elem: HTMLElement
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBApgGzgWxgXhgExMArsuMKAOgHM4oBRJAogIQE8BJTACgHIB3ACwEMoAtFACWBAcIjio7AJQBuAFAB6JTDUwAegH4YoSLEQoAXDAASAFQCyAGWopCsAD4wwuBAgXCAZjFYBCQ2QZGChuACcQThc4KMowiLCOAFUwXgAjJBCQGC9hMEwYAGIefiFROHFJYWl5BUDiPLA4MIsbdBh2AAVeMKgGGHNy9mIMvIBrVlqVTR09aHgaE1bbGgcFIA)

----

```ts
function contains(text: string, search: string | RegExp) {
  if (search instanceof RegExp) {
    return !!search.exec(text);
    //       ^? (parameter) search: RegExp
  }
  return text.includes(search);
  //                   ^? (parameter) search: string
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABBBUCGMwGcAUUCmAHlAFyJZQBOmA5gDTn5qUQAWZF1YNiAPogCV8NAKKEADgEpEAbwBQiRDGCIcWJi1ZLs6SPjgqhoidPmLFlfFBCUkAQjvrmbAHRF8EPESiSA3AvMAekDzUIA9AH5VcWY0AFsrfEppJ00yIzFxAIBfAMtrW0QCYhdMCAAbEAATfFxUtj8A4NCW1vConBjKeMTkxmd2cipaOVygA)

----

```ts
interface Apple { isGoodForBaking: boolean; }
interface Orange { numSlices: number; }
function pickFruit(fruit: Apple | Orange) {
  if ('isGoodForBaking' in fruit) {
    fruit
    // ^? (parameter) fruit: Apple
  } else {
    fruit
    // ^? (parameter) fruit: Orange
  }
  fruit
  // ^? (parameter) fruit: Apple | Orange
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgIIAd0BsUG9nADOA4gPakAmAYqVAEJwDWoA5gFzIBG5OcIA3MgC+AKFCRYiFAHkofFnmQgArgFsAylmBJCHFas7RBomMpAIwwUiGTptjKlGXAwAChhOXHDNhQAfZFl5CABKZFwRZAIYZFcAciIyShp6JlY4ghsPZzAwiKio7JdIgoB6UuQAPQB+WPQ4OVUICTCisG9MHBKhZAgsQjwSws8wIeRyqtrXesbm6FaRjiCQBW6StpKJmrqGuCaW5DaO32QA5dXRIA)

----

```ts
function contains(text: string, terms: string | string[]) {
  const termList = Array.isArray(terms) ? terms : [terms];
  //    ^? const termList: string[]
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABBBUCGMwGcAUUCmAHlAFyJZQBOmA5gDSIGUC2WZF1YNiAPuVbQDaAXQCUiAN4AoRMgQVG+FgBkYCgLyIAgpUpoAngDo1OvfrxLW4gPyKWWRGUFNWwgNwzEAei+zZAPVsUbCg7ZlUKdgEuEU8fRENEqQBfKSA)

----

```ts
//because typeof null is "object" in javascript, you have not, in fact, excluded null with this check.
const elem = document.getElementById('what-time-is-it');
//    ^? const elem: HTMLElement | null
if (typeof elem === 'object') {
  elem;
  // ^? const elem: HTMLElement | null
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBApgGzgWxgXhgExMArsuMKAOgHM4oBRJAogIQE8BJTACgHIB3ACwEMoAtFACWBAcIjio7AJQBuAFAB6JTDUwAegH4YoSLEQoAXDAASAFQCyAGWopCsAD4wwuBAgXCAZjFZQGAA5wID6GqGgRMOwgAEYAVnDA0jIwAN4KamGKaiqaOnrQ8DQmFjZ2tE4ubh4AvgpAA)

----

```ts
function maybeLogX(x?: number | string | null) {
  if (!x) {
    console.log(x);
    //because empty string and 0 are both falsy, x could still be a string, or number
    //          ^? (parameter) x: string | number | null | undefined
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAWwIYE8BGBTAMnAcwA0AKADwH4AuRMEZHAJ0QB9EBnKRmMA12kABtBASkQBvAFCJEMYIhIBCMmKkyZEBOziDsAOkGFyIgNzT1Aegvqb6gHoUFAB1SNUybFGyMxZGp25efjoGb2ChQX5wABNsYB5saPMAX0lUoA)

----

```ts
// this is known as "tagged union" or "dicriminated union"
interface UploadEvent { type: 'upload'; filename: string; contents: string }
interface DownloadEvent { type: 'download'; filename: string; }
type AppEvent = UploadEvent | DownloadEvent;

function handleEvent(e: AppEvent) {
  switch (e.type) {
    case 'download':
      console.log('Download', e.filename);
      //                      ^? (parameter) e: DownloadEvent
      break;
    case 'upload':
      console.log('Upload', e.filename, e.contents.length, 'bytes');
      //                    ^? (parameter) e: UploadEvent
      break;
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgKoAcA2B7OATAUQDcJxkBvZMAT3QgC5kByAVy1zyYG5kZhNScALYNkAZzBRQAcx4Js4UmDGMJUkNOQBfAFChIsRCgAi2AO4gc+YkopVaopnnOWO3Xv0EjVkmT100dMgAgujoNmQAvGjs1iRkAD7IphZWhPFgXDo6MCwgCGDACsgAFnAgeAIRYAAUoqHhGQCUFDrI4mbAYAglyHUAdIEQLeRt7cgIcGIoTi5pTPRj4xMKYtgC-TjSNUwprvhMADTIEP18AiDCw1nL7QD0d7dPz8sAegD8fehwUFcGLaI9mlqktxgAjKAQOAAaxu40m02YbHmiye8hAaw2Wx2GHmx1O5y8EHx-XRkHAYk2pGkYBKxyYYOokDETCacOWDxeXPGHy+Pz+0ABjFxHBBTwhUNhY10uiAA)

----

```ts
function isInputElement(el: Element): el is HTMLInputElement {
  return 'value' in el;
}

function getElementContent(el: HTMLElement) {
  if (isInputElement(el)) {
    return el.value;
    //     ^? (parameter) el: HTMLInputElement
  }
  return el.textContent;
  //     ^? (parameter) el: HTMLElement
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABDAzgSTABxFAogGwFMBbQsKACkPwC5ECSyoBKO65FRACQBUBZADIZseIqXKIA3gChEiAE6EoIeUgDkANwCG+EITXIk1ANzSAvtOmhIsBIgDmShuKgBhBFCZVa3fgOdMzFKyyMCIFKjCOAHk3sxBMnJyisqqiNQAdNq6hKZJiAD0BfmIAHoA-OGYWvJapJ7yQdR0vIJRoozkIRbJSipG+BmeAB5uHkx5hcX5FVU1dUqEjek+rf5iTObSQA)

----

```ts
const formEls = document.querySelectorAll('.my-form *');
const formInputEls = [...formEls].filter(isInputElement);
//    ^? const formInputEls: HTMLInputElement[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABDAzgSTABxFAogGwFMBbQsKACkPwC5ECSyoBKO65FRACQBUBZADIZseIqXKIA3gChEiAE6EoIeUgDkANwCG+EITXIk1ANzSAvtOmhIsBIgDmShuKgBhBFCZVa3fgOdMzFKyyMCIFKjCOAHk3sxBMnJyisqqiNQAdNq6hKZJiAD0BfmIAHoA-OGYWvJapJ7yQdR0vIJRoozkIRbJSipG+BmeAB5uHkx5hcX5FVU1dUqEjek+rf5iTObSEAgoUIjAcPLEBJwAvIgAJnAQIC4ZAI568gCeAMrUhNBHAIL4+BQ1BliC8ALSHY6IABUamYph2YD2ByOxHap0QFwA2hkcRCTvgUABdDLAGD4BoRdBYaIbchw6RFGaVBFIvFogktPzszpQTGE6RAA)

----

```ts
const nameToNickname = new Map<string, string>();
declare let yourName: string;
let nameToUse: string;
if (nameToNickname.has(yourName)) {
  nameToUse = nameToNickname.get(yourName);
  // ~~~~~~ Type 'string | undefined' is not assignable to type 'string'.
} else {
  nameToUse = yourName;
}

const nickname = nameToNickname.get(yourName);
let nameToUse: string;
if (nickname !== undefined) {
  nameToUse = nickname;
} else {
  nameToUse = yourName;
}

// this pattern is common and can be written more concisely using the "nullish coalescing" operator (??)
const nameToUse = nameToNickname.get(yourName) ?? yourName;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBGCGBbApgFRAOQJbANYJRgF45kB3GAWXgAcAeaAJyzAHMAaGJl1gPgAoAlAG4AUABNkwADbxGyGNOSwAniACujDEmQAuLlGZsxoSLAJoQAVQgKSF9NjwWAdK2X81m7SkEwA-P4wXlo6YkA)

----

```ts
function logLaterIfNumber(obj: { value: string | number }) {
  if (typeof obj.value === "number") {
    setTimeout(() => console.log(obj.value.toFixed()));
    //                                     ~~~~~~~
    // Property 'toFixed' does not exist on type 'string | number'.
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAGzgcwDIEMoFMBOAksAHIgC2ARgQBRyUBWAXIgN6IBuWyIuLAzlHwwwaRAB9EYCtXyIAvgEo2AKESIYwRDSgBPAA644W+gwB0XHrkQBeO4gBE0qgQfLWa9Yn64oAFRhyIxAoGhplGwA+RAgEfjhkXDNUNDpGC25eMyg4ADEYAA9cABNwxUUAbk91AHoarwbGpuaWhoA-Ds626sQ6xAAFfDhDfD1EAHIc-KLi8cRiuFx+KTgoRFwCmEFEBEQ9QwnBYVEJKRkCcbNPeRUboA)

----

```ts
const obj: { value: string | number } = { value: 123 };
logLaterIfNumber(obj);
obj.value = 'Cookie Monster';

// by the time the callback runs, the type of obj value has changed, invalidating the refinement. This code throws an exception at runtime, and TypeScript is right to warn you about it.

```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAGzgcwDIEMoFMBOAksAHIgC2ARgQBRyUBWAXIgN6IBuWyIuLAzlHwwwaRAB9EYCtXyIAvgEo2AKESIYwRDSgBPAA644W+gwB0XHrkQBeO4gBE0qgQfLWa9Yn64oAFRhyIxAoGhplGwA+RAgEfjhkXDNUNDpGC25eMyg4ADEYAA9cABNwxUUAbk91AHoarwbGpuaWhoA-Ds626sQ6xAAFfDhDfD1EAHIc-KLi8cRiuFx+KTgoRFwCmEFEBEQ9QwnBYVEJKRkCcbNPeRUb2LBt0xZ2S14BIRExSWdZBVs2TiZPiIACMACYAMwKKopbB4Iikc74NIMSoqUwZKz-cYAYTgcAA1jBrABZOLw8ZVIA)


# Be Consistent in Your Use of Aliases

## Things to Remember

- Aliasing can prevent TypeScript from narrowing types. If you create an alias for a variable, use it consistently.
- Be aware of how function calls can invalidate type refinements on properties. Trust refinements on local variables more than on properties.


## Code Samples

```ts
const place = {name: 'New York', latLng: [41.6868, -74.2692]};
const loc = place.latLng;
// you have created an alas, changes to the properties on the alias will be visible on the original value as well
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBADgGwIbAKYwLwwN5iQW1QC4YByAOVQHcYBNEAJwGtSAaGZKAGTAHMSA2gBYAjADoAbAA5p7ALQB2IWIBMEgJwqAugF8A3AChQkWAhDBM8ZGjGcevQ0A)

----

```ts
interface Coordinate {
  x: number;
  y: number;
}

interface BoundingBox {
  x: [number, number];
  y: [number, number];
}

interface Polygon {
  exterior: Coordinate[];
  holes: Coordinate[][];
  bbox?: BoundingBox;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHt1QCajpZAbwChlkAPALmRAFcBbAI2gG5TkBPaup14gX2LFQkWIhQAhdLRC4QAcynki7KsgDaPZlAA0NBtoC6bMlw1boei1GMChI6PCTIACugA2HeehAqyEclFgLGoMLDl8CHVbMgALDwgAZ1DMHDxIaOiTZEZGdHIAfmopGTlFfLZBIA)

----

```ts
function isPointInPolygon(polygon: Polygon, pt: Coordinate) {
  if (polygon.bbox) {
    if (pt.x < polygon.bbox.x[0] || pt.x > polygon.bbox.x[1] ||
        pt.y < polygon.bbox.y[0] || pt.y > polygon.bbox.y[1]) {
      return false;
    }
  }

  // ... more complex check
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHt1QCajpZAbwChlkAPALmRAFcBbAI2gG5TkBPaup14gX2LFQkWIhQAhdLRC4QAcynki7KsgDaPZlAA0NBtoC6bMlw1boei1GMChI6PCTIACugA2HeehAqyEclFgLGoMLDl8CHVbMgALDwgAZ1DMHDxIaOiTZEZGdHIAfmopGTlFfLZBGBkEMGDfYES3EQBJEDdPbxAACgAHDy8fag7BkD1esBTw9IgASj9kYBhkPoGugDpc-PmSMjIllYn15QAeZH7On0288mP1AAZDZAAfZ-OwY+QAPnO1q63buR1ABGJ6vdh7PZHDjIM4XUbXfLrDgPMFvaHfX6XECI24o0E7CF7KAQMC0KC+eDuRIQbJkQT0oRkAD0zOQ6w5yHoWBQCHQ9F67gCyAQsQgCAA1nYgA)

----

```ts
function isPointInPolygon(polygon: Polygon, pt: Coordinate) {
  polygon.bbox
  //      ^? (property) Polygon.bbox?: BoundingBox | undefined
  const box = polygon.bbox;
  //    ^? const box: BoundingBox | undefined
  if (polygon.bbox) {
    console.log(polygon.bbox);
    //                  ^? (property) Polygon.bbox?: BoundingBox
    console.log(box);
    //          ^? const box: BoundingBox | undefined
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHt1QCajpZAbwChlkAPALmRAFcBbAI2gG5TkBPaup14gX2LFQkWIhQAhdLRC4QAcynki7KsgDaPZlAA0NBtoC6bMlw1boei1GMChI6PCTIACugA2HeehAqyEclFgLGoMLDl8CHVbMgALDwgAZ1DMHDxIaOiTZEZGdHIAfmopGTlFfLZBGBkEMGDfYES3EQBJEDdPbxAACgAHDy8fag7BkD1esBTw9IgASj9kfs6fADpc-PYAek2yXeQAPQLkPqh0XugwDnmRrrW8wuLpWVBy5QAfZFKIGFAIbHYED5EmAcvlkABeRYDW7rcjZbZ7Q7IQEgYGgtQlZ4KJTID5fH4gP7sYAwY5LUZ3fLzEh7FGJBIrdzoeR9aGrWGzbJkBF7Xl8shIk5nC5XVxskCUh7ITFlJTsMh0hlMln3Tny5A8-kHI50kH3R6lF44vGyb6-f5kQSCIA)

----

```ts
// if you introduce an alias, use it consistently
function isPointInPolygon(polygon: Polygon, pt: Coordinate) {
  const box = polygon.bbox;
  if (box) {
    if (pt.x < box.x[0] || pt.x > box.x[1] ||
        pt.y < box.y[0] || pt.y > box.y[1]) {  // OK
      return false;
    }
  }
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHt1QCajpZAbwChlkAPALmRAFcBbAI2gG5TkBPaup14gX2LFQkWIhQAhdLRC4QAcynki7KsgDaPZlAA0NBtoC6bMlw1boei1GMChI6PCTIACugA2HeehAqyEclFgLGoMLDl8CHVbMgALDwgAZ1DMHDxIaOiTZEZGdHIAfmopGTlFfLZBGBkEMGDfYES3EQBJEDdPbxAACgAHDy8fag7BkD1esBTw9IgASj9kBB9EsBz85ABeZH7OnwA6XIr2YBhkbrzyeZIyMhOzib3lAB418kf1AAZDZAAfH+2wI9kAA+V7vACM3z+7BuNweHGQLwuew4nyh-3hILBqMhVzIAHp8cgAPIAaRhNygEDAtCgvng7kSEGyZEErPYhOQe25diAA)


----

```ts
function expandABit(p: Polygon) { /* ... */ }

polygon.bbox
//      ^? (property) Polygon.bbox?: BoundingBox | undefined
if (polygon.bbox) {
  polygon.bbox
  //      ^? (property) Polygon.bbox?: BoundingBox
  expandABit(polygon);
  // the call to expandABit could very well unset polygon.bbox, so it would be safer for the type to revert to BoundingBox | undefined. BUt this means that you would need to repeat your property checks every time you called a function. So Typescript, makes a pragmatic choice to assume the function does not invalidate its type refinements.
  // you could pass read only version of polygon to the function. By preventing mutation, we also improve type safety.
  polygon.bbox
  //      ^? (property) Polygon.bbox?: BoundingBox
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHt1QCajpZAbwChlkAPALmRAFcBbAI2gG5TkBPaup14gX2LFQkWIhQAhdLRC4QAcynki7KsgDaPZlAA0NBtoC6bMlw1boei1GMChI6PCTIACugA2HeehAqyEclFgLGoMLDl8CHVbMgALDwgAZ1DMHDxIaOiTZEZGdHIAfmopGTlFfLZBAHoq5AAJAEkAEQBRYgQfRLBkAAcPLx9qN09vXwBeImQAoJCNQz149yTqaOR+NhgZBDBg3wQ4dwRad0jhgZAJPPIACj6Rwdd+0YBKImraloA5JvbO7sJcvl+MgJndzmxgDBkNcAISA8ivEhkfaHY6nJ4+S75W4YkDPFhkGrIABiwHc7kSyFAvVxADp4ewiZ90AB3Gn3ED0q7IOCyHLcqAQGDQZBgdDIXAwYWC8DIABuB1oSRhdmImxA212U3IPV52AAghJgGBbkNcYjkFUAFTIWl25BW2qCYhg0Zc-LEIlkb0APQK0J6UHQPWgYA4rzObvhRWQJVkoHKygAPshSkLQBBsMIoTiOe6EX52ed84zat6yH6A0GQ1AwxG6dHitJ4wolOwArrZIbjbnzvj2K6fCXCWXy5XbtXQ+HHnnG7Hm2U24IgA)


# Understand How Context Is Used in Type Inference

## Things to Remember

- Be aware of how context is used in type inference.
- If factoring out a variable introduces a type error, maybe add a type annotation.
- If the variable is truly a constant, use a const assertion (`as const`). But be aware that this may result in errors surfacing at use, rather than definition.
- Prefer inlining values where it's practical to reduce the need for type annotations.

## Code Samples

```ts
function setLanguage(language: string) { /* ... */ }

setLanguage('JavaScript');  // OK

let language = 'JavaScript';
setLanguage(language);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwKZQDIEMwHMRa6oAUANjvoagFwpQBOMeAlIgN6ID0AVIgHQDE3TogC+AKHFpMFAkWIByAFJYAblgDKERgAcoC5gG5EXEQHkA0pNLpE5PHNSIAvImVrN2mHoWGp6bAcqMlkqIxNOcysgA)

----

```ts
type Language = 'JavaScript' | 'TypeScript' | 'Python';
function setLanguage(language: Language) { /* ... */ }

setLanguage('JavaScript');  // OK

let language = 'JavaScript';
setLanguage(language);
//          ~~~~~~~~ Argument of type 'string' is not assignable
//                   to parameter of type 'Language'
// Typescript determines the type of a variable when it is first introduced (unlike some languages are able to infer types for variables based on their eventual usage.)
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSZLUNC2MdfCJSSho6K3EoR28AeQBpfz11KAMtYyhsMOIOKIkA9U0jXUyy6ykHbzi6+oA-JuamqABBClQAWwgEYChhaShQSFwVYGpkeioVKARhfrgVFSokBDgAIzTJGvq9-frgYSgwOAo4HuAICgGhkegcUsscSSA)

----

```ts
let language: Language = 'JavaScript';
setLanguage(language);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSXvUoAy1jM00jDChsfCJSSho6KTUNC2N9VIwrcShHbwB5AGlJIA)

----

```ts
const language = 'JavaScript';
//    ^? const language: "JavaScript"
setLanguage(language);  // OK
// By using const, we've told the type checker that this variable cannot change. So TypeScript can infer a more precise type for language.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSWVEVYCgDLWMobHwiUkoaOikHbyhkgD0AfigAhCCQi2MzACICYg44gsk1DTzdUKMMK3FkxKgAeQBpSSA)

----

```ts
// Parameter is a (latitude, longitude) pair.
function panTo(where: [number, number]) { /* ... */ }

panTo([10, 20]);  // OK

const loc = [10, 20];
//    ^? const loc: number[]
panTo(loc);
//    ~~~ Argument of type 'number[]' is not assignable to
//        parameter of type '[number, number]'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSQ+9eOAo4AFt1CAooKhUoOCh9OEVgFAATCAAaKD1RJCoU9JswOCoKVxk5BSUEKGKEZmEdAHdBSNMoAG0EFFCAI0is7r7IgF0be2c3Dy9fSUk6hp0OgEYABiyAJlWx8ShHbwB5AGk5slEVYGzhMihsFfWoLZGpAL29gD0AfigzhAurshmIb9CgdEbzRCLHJkKwvbxvAB+SKgAEEKKhwghLsJpFBQJBcMDImD6DEoAhhJc4CoVFQkAg4L09NBgMJ-PC3m9iiFwsBIlAcXi2Lguj0QYMxaMcJIgA)

----

```ts
const loc: [number, number] = [10, 20];
panTo(loc);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSQ+9eOAo4AFt1CAooKhUoOCh9OEVgFAATCAAaKD1RJCoU9JswOCoKVxk5BSUEKGKEZmEdAHdBSNMoAG0EFFCAI0is7r7IgF0be2c3Dy9fSTJRFWBs4TIzLp7+ikGN0ahsDoBGAAYsgCYjkak6hv0Vq3EoR28AeQBpSSA)

----

```ts
const loc = [10, 20] as const;
//    ^? const loc: readonly [10, 20]
panTo(loc);
//    ~~~ The type 'readonly [10, 20]' is 'readonly'
//        and cannot be assigned to the mutable type '[number, number]'
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgAZigRlgVUVADOEYPGRoMACgA2iVOggAuWIe0QAlFADeUAPQAqKADp3UJw6gBfSQ+9eOAo4AFt1CAooKhUoOCh9OEVgFAATCAAaKD1RJCoU9JswOCoKVxk5BSUEKGKEZmEdAHdBSNMoAG0EFFCAI0is7r7IgF0be2c3Dy9fSTJRFWBs4TIobA6ARgAGLIAmLZG42PmERakAqEuoAD0AfigTxeWyMwoIOFTRPRBO7b2DyR1Br6FZWc7eK4AP2hUGYrSgoEguDeHy+P02Oyg+xG9BiyPenwQ3xw-ghVyuiFSD0QCGES36RxUVCQCAgVOAwgR8NCKGAcF6emgiOgOC6PX6FEG4tGJKAA)

----

```ts
function panTo(where: readonly [number, number]) { /* ... */ }
const loc = [10, 20] as const;
panTo(loc);  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwIZgCpwBQHcAWApgE6EBcipqAJggDYCeiA2mCALYBGJANIm1xIBdAJSIA3ogD0AKkQA6RYhlTEAXwBQEBAGcoiOnAiIAvCwCMABj4AmS0MSodibWD0BuDWkw5DEEe6I0qoA8gDSGkA)

----

```ts
const loc = [10, 20, 30] as const;  // error is really here.
panTo(loc);
//    ~~~ Argument of type 'readonly [10, 20, 30]' is not assignable to
//        parameter of type 'readonly [number, number]'
//          Source has 3 element(s) but target allows only 2.
// const contexts can neatly solve issues around losing context in inference, but they do have an unfortunate downside, if you make a mistake in the definition (say you add a third element to the tuple), then the error will be flagged at the call site, not at the definition. This may be confusing, especially if the error in a deeply nested object that's used for from where it's defined. For this reason, it's preferable to use the inline form or apply a type declaration.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwIZgCpwBQHcAWApgE6EBcipqAJggDYCeiA2mCALYBGJANIm1xIBdAJSIA3ogD0AKkQA6RYhlTEAXwBQEBAGcoiOnAiIAvCwCMABj4Ama4gDMloYlQ7E2sHoDciaapJiOGJEGHcqOkZEIlJ5DTRMHEMIEW8NKVU-RAA-XMQAQWIAcw5CMH04YEQoBmRCRAByKlowKOYrW3snIQbQ9zA4fTcdGCKwVE46eqg4dMysrLRiVHZCKBJESura+qbCGnomVg5uYj4BU565hZvEAGU4EGIIevw3R0RCKdXy7B0xTggfRQVDFNauSJwXDuQ6IGxxIA)

----

```ts
type Language = 'JavaScript' | 'TypeScript' | 'Python';
interface GovernedLanguage {
  language: Language;
  organization: string;
}

function complain(language: GovernedLanguage) { /* ... */ }

complain({ language: 'TypeScript', organization: 'Microsoft' });  // OK

const ts = {
  language: 'TypeScript',
  organization: 'Microsoft',
};
complain(ts);
//       ~~ Argument of type '{ language: string; organization: string; }'
//            is not assignable to parameter of type 'GovernedLanguage'
//          Types of property 'language' are incompatible
//            Type 'string' is not assignable to type 'Language'
//as before, the solution is to add a type annotation (const ts: )
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAMghgOwOYFc5OgXigcgFJwBucAygMYBOAlmMDlAD64Aq4E51t9TOACiMAAWAewQ4A3ACgqCYBAoAzOGWgBxYYXkIIAE3jI0GKAG9JUKABtEqdBABcsa4YhTzwikkRUAXnGBVRBwBnYGpkKQBfSUkFFAQyf1EoMmEAWzArGQAKKwNbB3VNCm09J1sAShMoAHoAKigAOiaoWuqoKMkU9MyELONLMowHHFZIDho6ABood08EHz8AhGGAWSpKYSDhBTp28vFzaraAeQBpaJSEEKhgIKhsU3NcmyGWNnGuSbMZjy9fROWuDWGy2OxwXwiUi6GTg2Vu+0kR3MyPMAD9UVAAIIeFCpCCyGYKG5sXD9Z7OYKhGRIA6zP6LQJQEJhGntHCItoornmKh3BDCYBQOBBIJUJAIOAAIws0GAwigYDgFDgeLkFEJxMguEKWl0+heEHZSO5yNGEDu2wVFGEkAooFw5Ns9CV0Bk0MW0ogHJNXLNuGZ1PovKg-MFwtF4qlMpu8tAWpw+uc7KAA)

----

```ts
function callWithRandomNumbers(fn: (n1: number, n2: number) => void) {
  fn(Math.random(), Math.random());
}

callWithRandomNumbers((a, b) => {
  //                   ^? (parameter) a: number
  console.log(a + b);
  //              ^? (parameter) b: number
  // when you pass a callback to another function, TypeScript uses context to infer the parameter types of the callback
  // if you factor the callback out into a constant, you lose that context and get noImplicitAny errors
  // if the function is only used in one place, prefer the inline form since it reduces the need for annotations
});
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABBAhgGzQdRlAFgJRTABM4BbAORDICMBTAJwGcAKYMALkRbAEYuw1egwA0iMACYBQxgEpEAXgB8iAG5wYxeQG8AUIkTsWAWRR4AdAyKkyLWWNMWrJcndkBuXQF9du1Bmw8QhdKGWYWFhQxGnllRD0DAHpEg1S09PSAPQB+bgAHFCsyOig5RBRpWkZ9ZAQmODQ6czQ4AHNIxABqRBjPJJSMwZz8wpRi0oZ5Gkrhbw9dIA)

----

```ts
const fn = (a, b) => {
  //        ~    Parameter 'a' implicitly has an 'any' type
  //           ~ Parameter 'b' implicitly has an 'any' type
  console.log(a + b);
}
callWithRandomNumbers(fn);
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABBAhgGzQdRlAFgJRTABM4BbAORDICMBTAJwGcAKYMALkRbAEYuw1egwA0iMACYBQxgEpEAXgB8iAG5wYxeQG8AUIkTsWAWRR4AdAyKkyLWWNMWrJcndkBuXQF9dEBEyhDJAVuFDEaeWVEPQMAeliDRMSAPySABRQrMjooRkQAchR8xBgyAAc0GAgcNABPRFwUJkQiAqJa4qhasrp9RHikwYNUjKycvPyaYtKKqpr6xubWwrAOxC6evr8wJjg0OnM0OABzFhREAGpECM8fVAxsPEIXShlmNjAPXSA)

----

```ts
const fn = (a: number, b: number) => {
  console.log(a + b);
}
callWithRandomNumbers(fn);
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABBAhgGzQdRlAFgJRTABM4BbAORDICMBTAJwGcAKYMALkRbAEYuw1egwA0iMACYBQxgEpEAXgB8iAG5wYxeQG8AUIkTsWAWRR4AdAyKkyLWWNMWrJcndkBuXQF9dEBEyhDJAVuFGlaRjEacOF5ZUQ9Az8wJjg0OnM0OABzFhREAGpEGg9vX3QsHAJrcioI5jYwUqA)


# Understand Evolving types

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
  - While TypeScript types typically only refine, the types of values initialized to null, undefined, [], any and any[] types are allowed to evolve. 
  - You should be able to recognize and understand this construct where it occurs. and use it to reduce the need for type annotations in your own code.
  - For better error checking, consider providing an explicit type annotation instead of using evolving any.


# Use Functional Constructs and Libraries to Help Types Flow

## Things to Remember

- Use built-in functional constructs and those in utility libraries like Lodash instead of hand-rolled constructs to improve type flow, increase legibility, and reduce the need for explicit type annotations.
- JavaScript has never included the sort of standard library you find in Python, C, or Java. Over the years, many libraries have tried to fill the game. JQuery provided helpers not just for interacting with the DOM but also for iterating and mapping over objects and arrays. Underscore focused more on providing general utility functions, and Lodash built on this effort. Today libraries like Ramda continue bring ideas from functional programming into JavaScript world. 

## Code Samples

```js
const csvData = "...";
const rawRows = csvData.split('\n');
const headers = rawRows[0].split(',');

const rows = rawRows.slice(1).map((rowStr) => {
  const row = {};
  rowStr.split(",").forEach((val, j) => {
    row[headers[j]] = val;
  });
  return row;
});
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimky4OZV0ttDJp37BFggIyS8AWxQuQUEHGgBlKEpJLAA+GABvEhg4OypGFniAX1Jk0IjKU34hHAscXwAzEEoAURRgeWCEFB4LGAAraMw4xOTcxj0lVXV9NqMjFiaeHJhM6SSYSkUoAFdKMAXGUlnSIA)

----

```ts
import _ from 'lodash';
const rows = rawRows.slice(1)
    .map(rowStr => _.zipObject(headers, rowStr.split(',')));
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCMuBynkws2gxMnPzAioIAjJIkMOkweLYoXIIRAMpQlFgAfDDOeABefFwA8gBGAFaKwEJKquoQFjAFRab8QsJWkiOkQA)

----

```ts
const rowsImperative = rawRows.slice(1).map(rowStr => {
  const row = {};
  rowStr.split(',').forEach((val, j) => {
    row[headers[j]] = val;
    // ~~~~~~~~~~~~ No index signature with a parameter of
    //              type 'string' was found on type '{}'
  });
  return row;
});
const rowsFunctional = rawRows.slice(1)
  .map((rowStr) =>
    rowStr
      .split(",")
      .reduce(
        (row, val, i) => ((row[headers[i]] = val), row),
        //                 ~~~~~~~~~~~~~~~ No index signature with a parameter of
        //                                 type 'string' was found on type '{}'
        {}
      )
  );
  // the solution in each case is to provide a type annotation for {}, either {[column: string]: string} or Record<string, string>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCMuBynkwAkvbqaHwIiizaDEyc-MCKggCMkni2KFyCEQDKUJRYAHwwAN4kMHBhVIws1QC+pPUlZab8QsJWuW6OAKIowPKCgggoPBYwAFaSlTV19TARekqq6vrzRkYs0zwdawD0pzAAftc3t9cwAHIgMHxgagAeMBB8AOZgaABXSiJGgCeQwDBcFDUWyKKDqGAgNyrernNbojH1KAATy4iWE0Eorx+whgNEC7hAALeiLAMBxeJ8bWEq1a0lWwKgQLpEVIbNCFHWugAYtTgFA+OAZklaCkIGk+BlspJVnkCpMupQlpgKiihTRSpQ9fUeuYcBYcCrMXhgSoAUrjWsiow5kc5nxtVUNYxNso1Bo9Hx9ocZpI5hEw47URdMbG1ncE7dHs9Xh8vr9-lzgWSwRCYFCYXCEUiozA0XGK5WMQz8YTiaTycwhtSVLT6bj8czS21HVaYOygA)

----

```ts
const rowsLodash =
  rawRows.slice(1).map(rowStr => _.zipObject(headers, rowStr.split(',')));
rowsLodash
// ^? const rowsLodash: _.Dictionary<string>[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCMuBynkwAMv6B8lgkMDDaDEyc-MCKggCMkni2KFyCEQDKUJRYAHwwzngAXnxcAPIARgBWisBCSqrqEBZJjKWUpvxCwlaSk6QRENEBQSQA9IswAHoA-HBhVLpzsQBc1XhIfJ184CiUAJ4APNCUfGAA5hV6RiRAA)

----

```ts
interface BasketballPlayer {
  name: string;
  team: string;
  salary: number;
}
declare const rosters: {[team: string]: BasketballPlayer[]};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCNmBQ6m4owIowAEKBANaKUABGKDw8AAo8KACe6jAA3iQwMGAotooAXDDQlHxgAOakpeEVNXUNzSW16SiUuTVgAK62KeqkAL4kasA5lDGyVCDQ6hA1hXptth1Q9U1GNfEQSanpWTn5lHpGk6RAA)

----

```ts
let allPlayers = [];
//  ~~~~~~~~~~ Variable 'allPlayers' implicitly has type 'any[]'
//             in some locations where its type cannot be determined
for (const players of Object.values(rosters)) {
  allPlayers = allPlayers.concat(players);
  //           ~~~~~~~~~~ Variable 'allPlayers' implicitly has an 'any[]' type
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCNmBQ6m4owIowAEKBANaKUABGKDw8AAo8KACe6jAA3iQwMGAotooAXDDQlHxgAOakpeEVNXUNzSW16SiUuTVgAK62KeqkAL4kasA5lDGyVCDQ6hA1hXptth1Q9U1GNfEQSanpWTn5lHpGk6Q8yTDn2XlrLDekAPSfpQB+-wDATAAGr9PgoFIPHzPS5rYQwOxmYACHi5BSBGBQXJcGLCFBgXI3YQkb6lMnk8kNWpeGJ+YBoPjgZg0JQLBFQZhYnFwfFgECwcYwNThSi2BqKFQkNyOGCCJYwXivDQwEBuGAAeRSACtFMAoHgEOlhooIIJPKsNJJJEUejClZonhkXlcIHhyPShIqXdIeqSKRTAYHfiCwRCoXinbCNPDEfxkVBUejmPjoQSiZjsYoSNMgA)

----

```ts
let allPlayers: BasketballPlayer[] = [];
for (const players of Object.values(rosters)) {
  allPlayers = allPlayers.concat(players);  // OK
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCNmBQ6m4owIowAEKBANaKUABGKDw8AAo8KACe6jAA3iQwMGAotooAXDDQlHxgAOakpeEVNXUNzSW16SiUuTVgAK62KeqkAL4kasA5lDGyVCDQ6hA1hXptth1Q9U1GNfEQSanpWTn5lHpGk6Q8yTDn2XlrR4nJaRkvVzcsN6Q3I4YIIljBeK8NDAQG4YAB5FIAK0UwCgeAQ6WGigggk8qw0kkkRR6z0uaxYpMhEDw5GAaEEEKuEGkpQA9Kz4QBpEjTIA)

----

```ts
const allPlayers = Object.values(rosters).flat(); // OK
//    ^? const allPlayers: BasketballPlayer[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCNmBQ6m4owIowAEKBANaKUABGKDw8AAo8KACe6jAA3iQwMGAotooAXDDQlHxgAOakpeEVNXUNzSW16SiUuTVgAK62KeqkAL4kasA5lDGyVCDQ6hA1hXptth1Q9U1GNfEQSanpWTn5lHpGkzLgcufZeWssAPIpAFaKwFB4COlhooIIJPKsNJI8G4ckJpDAAPTwmBvADSJERpVKAD0APxwB6wJ6XNZHRLJNIZZ5XG4kIA)

----

```ts
const teamToPlayers: {[team: string]: BasketballPlayer[]} = {};
for (const player of allPlayers) {
  const {team} = player;
  teamToPlayers[team] = teamToPlayers[team] || [];
  teamToPlayers[team].push(player);
}

for (const players of Object.values(teamToPlayers)) {
  players.sort((a, b) => b.salary - a.salary);
}

const bestPaid = Object.values(teamToPlayers).map(players => players[0]);
bestPaid.sort((playerA, playerB) => playerB.salary - playerA.salary);
console.log(bestPaid);

// better option,

const bestPaid = _(allPlayers)
  .groupBy(player => player.team)
  .mapValues(players => _.maxBy(players, p => p.salary)!)
  .values()
  .sortBy(p => -p.salary)
  .value();
console.log(bestPaid.slice(0, 10));
//          ^? const bestPaid: BasketballPlayer[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBMEDcAiBDKKYF4YCIB0BOA3AFCiSwBOKA7gEog0RZyKrp4QAOANgJZQAFAHIAOmGEBKUuWgwAFgFMUAE0WVm2avUYQA2gAYAup14CRAGimk+AWy4hKsAPowAZpRC2YwniBUoEPLCNmBQ6m4owIowAEKBANaKUABGKDw8AAo8KACe6jAA3iQwMGAotooAXDDQlHxgAOakpeEVNXUNzSW16SiUuTVgAK62KeqkAL4kasA5lDGyVCDQ6hA1hXptth1Q9U1GNfEQSanpWTn5lHpGkzLgcufZeWssAPIpAFaKwFB4COlhooIIJPKsNJI8G4ckJpDAAPTwmBvADSJERpVKAD0APxwB6wJ6XNZHRLJNIZZ5XG5kAkwcbQTIoPgqFjOQREl4Qnp4RqeYZcWK5QS8LlYAB8MFFVzw20kPNsKC4ADVAcCRcSNBKYM48IqAB5CjVciAWKXaricPoDSQAQnlpX+apBDpgnEcUCNXG1AFpLRBrblXU6eEDBNJaZAQDxFHg-I1BAyoEyWZx+NFBAYzQBGAySCMYzFF7F4pb04HJ5kqUkncmc6lGEhAA)


# Use async Functions Instead of Callbacks to Improve Type Flow

## Things to Remember

- Prefer Promises to callbacks for better composability and type flow.
- Prefer `async` and `await` to raw Promises when possible. They produce more concise, straightforward code and eliminate whole classes of errors.
- If a function returns a Promise, declare it `async`.


## Code Samples

```ts
declare function fetchURL(
  url: string, callback: (response: string) => void
): void;

fetchURL(url1, function(response1) {
  fetchURL(url2, function(response2) {
    fetchURL(url3, function(response3) {
      // ...
      console.log(1);
    });
    console.log(2);
  });
  console.log(3);
});
console.log(4);

// Logs:
// 4
// 3
// 2
// 1
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ojwIA)

----

```ts
const page1Promise = fetch(url1);
page1Promise.then(response1 => {
  return fetch(url2);
}).then(response2 => {
  return fetch(url3);
}).then(response3 => {
  // ...
}).catch(error => {
  // ...
});
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ohQ7DRRQeWREAAKeGQAFsdOhVOR5iYlsREaTyVSafTGQdMMZZGMoptGSRSBlOvYVJh8KhuqyBoiXvzBcLmqKpulQFLQDK5QrjGzwfAVQKhRs4gIJTquodjiq-D1rLI8DS8NrdfaDqbEUA)

----

```ts
async function fetchPages() {
  const response1 = await fetch(url1);
  const response2 = await fetch(url2);
  const response3 = await fetch(url3);
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ojwRToACeWnUwwaqG6JgACooPM1rDtfAxsFFNuhZCRyIoAO6KHTYeYmJbERH2QEc5pcqZsAVCkXlYzi35daWgTlxAR8wXC2mq3jgrqHY5PeBAA)

----

```ts
async function fetchPages() {
  try {
    const response1 = await fetch(url1);
    const response2 = await fetch(url2);
    const response3 = await fetch(url3);
    // ...
  } catch (e) {
    // ...
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ojwRToACeWnUwwaqG6JgACooPM1rDtQJg8KTQJ09oDsFFNuhZCRyIoAO6KHTYeYmJbERE8hh85oCqZsMUSqXlYyy34nXmgflxAQi8WS2na3jgk6HY72J6+RQ9UDWWSs+w2g5dJ7wb1AA)

----

```ts
async function fetchPages() {
  const [response1, response2, response3] = await Promise.all([
    fetch(url1), fetch(url2), fetch(url3)
  ]);
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ojwRToACeWnUwwaqG6JgACooPM1rDtfAxsABtKKbdCyGqgblxQYC5o82R8AC6bEUAHdFDpsHS8MgALY6XkHfwEawck7zExLYjJWrlYyG6YmnqG7ZdCWI+yHY5PeBAA)

----

```ts
function fetchPagesWithCallbacks() {
  let numDone = 0;
  const responses: string[] = [];
  const done = () => {
    const [response1, response2, response3] = responses;
    // ...
  };
  const urls = [url1, url2, url3];
  urls.forEach((url, i) => {
    fetchURL(url, r => {
      responses[i] = url;
      numDone++;
      if (numDone === urls.length) done();
    });
  });
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4oilYYNVDdEwABUUHmaAHUdJhjABhfxBEKhdDWHagS7YVA4AC20DQqnIAAYAQxsFFNuhmglMG5PABtAC6bDVku4oGkIrYXPSoE6e0B2GVMtaPgtk0GoGtcr46vI9uab3sh2O9ieWsYvHQGuqPgGQeWqrefoOamQeFgIWM1iWBB8OlSpAyxt28wqfV4VsNGb2LvQyp0Tocbt2-KFIoA1DWK-YdGpQNYq8LUKLSOQI5dPIzUrqO1yK5CvYinvAgA)

----

```ts
function timeout(timeoutMs: number): Promise<never> {
  return new Promise((resolve, reject) => {
     setTimeout(() => reject('timeout'), timeoutMs);
  });
}

async function fetchWithTimeout(url: string, timeoutMs: number) {
  return Promise.race([fetch(url), timeout(timeoutMs)]);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4oilYYNVCgXQAW1kyBwmGslOptIAsujQKgcBTArI8AVQAAFPDICk6dCyAA8qFkmW5GU69hUmHwZMlAHd+YLhaLrOMLtKfCoAFbyTCpUiyk4uQwAFR0VJpdOspoyhuN1goDPtFGSPg9zPQiPskKeSMU6AAnlp1CTRt0TAB1HSYYw2u20pZOFyYNyeH22xmYFnOdmc7k7UAKpXqoUiq54EKyawAbXmJnT3vJeft9M7fuSAF1EcGgA)

----

```ts
async function getNumber() { return 42; }
//             ^? function getNumber(): Promise<number>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ojwRToACeWnUwwaqFAHkM4hwAFtArI8NYOqAVJh8DS4cwaKAnji9iLdgA9AD8lLW+jpmAZzNZ7OcAAU8MhGTp0LIADyoJksvBpeBAA)

----

```ts
const getNumber = async () => 42;
//    ^? const getNumber: () => Promise<number>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ohQ7AeQziHAAW0CsjwbEU6AAnlpQNZUqQMnDmHRRLsAHoAfl8DBJZMp1LwETZGQACnhkBSdOhZAAeVBimlpeBAA)

----

```ts
const getNumber = () => Promise.resolve(42);
//    ^? const getNumber: () => Promise<number>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4ohQ7AeQziHAAW0CsjwbGsqVIGQACnhkBSdOgrlELplZNY4b8cbsAHoAfl8DBJZMp1LwEQZzNZ7M5AB5UDKaWl4EA)

----

```ts
// Don't do this!
const _cache: {[url: string]: string} = {};
function fetchWithCache(url: string, callback: (text: string) => void) {
  if (url in _cache) {
    callback(_cache[url]);
  } else {
    fetchURL(url, text => {
      _cache[url] = text;
      callback(text);
    });
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4og46BoCjYaTIUCYYw6dAAQih2AA+n4TPFQO0ANq8BKYNyeAC6vP5HiebHaTzodRG+nmJgA6jpqQBhELGWRLJwuPlJHx+ALBMIRTCyAAemGFSVSpAyRWkO1AOjUoE1jtQoBZatkDvs+qCIVC1k9bO5hAFiPsYtkBHQqk6ezlvSqhB8JvN6Q5J3swfVoYIArYacwbz2fsNgaLEd2kMj8Ce8CAA)

----

```ts
let requestStatus: 'loading' | 'success' | 'error';
function getUser(userId: string) {
  fetchWithCache(`/user/${userId}`, profile => {
    requestStatus = 'success';
  });
  requestStatus = 'loading';
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEAkEkBEFECgDGB7AdgZwC6gK4CcAbARlAF5QByIigbiTS10ICYzLnb6Nt8CBmNhT6cQoWADlo8ACYBTRAQCGeWaABmOVIkwBLNOtmZEACwCqAJQAyACnigmBAFygseHagDmAGlCJFBAgAjRUQAa2drFXQABwZZZ1d3DwBKMgA+UAA3ZB1peGTnbNy6eDVDEwsbXiIfDS1dNEjZGLiiVIBvOwMjMytrXmZazW09VCaWjFlmDq77Mp7K-sI+IfrR8djJvhn7XdBRADoj2d2UDGQCWQOCZA9rNro9gF9kx9OGC6ubu+m3l7ezuhPtdbtZtnR-lwgZcQXcACyveDwUSWW7oRzIsBwzGgPg45g4og46BoCjYaTIUCYYw6dAAQih2AA+n4TPFQO0ANq8BKYNyeAC6vP5HiebHaTzodRG+nmJgA6jpqQBhELGWRLJwuPlJHx+ALBMIRTCyAAemGFSVSpAyRWkO1AOjUoE1jtQoBZatkDvs+qCIVC1k9bO5hAFiPsYtkBHQqk6ezlvSqhB8JvN6Q5J3swfVoYIArYacwbz2fsNgaLEd2kMj8Ce8Eu2BUAEccM1MABlTCKTA4dGUG6KaRJCigAA+lHQOEQiGa6FHE4osjweGQeE40oa7o8hlMsbw-X3kGkls8DsTipVXusAANgH3l8AACTtB94Y9PG8+aKrtQ6S4ZvGuwtm2WBdj2faCFOM5zpwkZViB7bgb26CCIOw6eJw9ZAA)

----

```ts
const _cache: {[url: string]: string} = {};
async function fetchWithCache(url: string) {
  if (url in _cache) {
    return _cache[url];
  }
  const response = await fetch(url);
  const text = await response.text();
  _cache[url] = text;
  return text;
}

let requestStatus: 'loading' | 'success' | 'error';
async function getUser(userId: string) {
  requestStatus = 'loading';
  const profile = await fetchWithCache(`/user/${userId}`);
  requestStatus = 'success';
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/MYewdgzgLgBA+sAhsAFgUwFwwN4G0CuATgDZbSECWYA5gLplSU0C+MAvDswNwBQiEATzDAYAM3zCoFcGLRRUAdQpQUAYWToAFEVIxyVagEocPGDAqiY2kubDwkqNMeymzMQnKJ2EGtARK0vGbMrqCQsB4QAA7gEGjsMIgA7ojKsvIo1sSGQTBh0DBQaAAesBzJqRFo0bFoAHRFpZo5rj6O-sS0CY1QuR5QXoUlvTwhPMRy7mgAjvjVUADKUIgDEFgA5MQgiAAmBuswAD4w6xD4wMDVEAfH62iEhCCE67z8QiLiktJ21HIAqnFCNpAQBJHYMJhGExmDyzeZLFb4CAJTbbPY0F6hWKwKKPUQUCYJCppURyRTKNS+TQAAwA9Ej7rSACTYBmEMHMaktGEzObQBGrFFnC5XTEhIA)

----

```ts
async function getJSON(url: string) {
  const response = await fetch(url);
  const jsonPromise = response.json();
  return jsonPromise;
  //     ^? const jsonPromise: Promise<any>
}
getJSON
// ^? function getJSON(url: string): Promise<any>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/IYZwngdgxgBAZgV2gFwJYHsIwOYFNkBSAygPIByAFAgE4A2AXDCMtahNgJQwDeAUDDCiZmMarhAAHYbhgBeGMADuwVMnj4oACyp0OAbn6DhagFYhMABWroAtqhAz5YydIB0ZzBX2GxyGlg8IK1t7XAMBAHoIgRiAPQB+IwgRQOC7B0Y00IAeYAgwAD5eAF9ePEJSMl4omAT4JCg0TBx8YnIdBiYWNk5M63TcXPyioA)


# Use Classes and Currying to Create New Inference Sites

## Things to Remember

- For functions with multiple type parameters, inference is all or nothing: either all type parameters are inferred or all must be specified explicitly.
- To get partial inference, use either classes or currying to create a new inference site.
- Prefer the currying approach if you'd like to create a local type alias.

////
// verifier:reset## Code Samples

```ts
export interface SeedAPI {
  '/seeds': Seed[];
  '/seed/apple': Seed;
  '/seed/strawberry': Seed;
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eEA)

----

```ts
declare function fetchAPI<
  API, Path extends keyof API
>(path: Path): Promise<API[Path]>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDEA)

----

```ts
fetchAPI<SeedAPI>('/seed/strawberry');
//       ~~~~~~~ Expected 2 type arguments, but got 1.
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDCVllWrVEVWTXrac-kFQoZoLDNGEL4QAfh+fb8gAoiIpkGwACZkGAQsIUOkaFk2OByI0AllJDRRJIAIyxPBAA)

----

```ts
const berry = fetchAPI<SeedAPI, '/seed/strawberry'>('/seed/strawberry');  // ok
//    ^? const berry: Promise<Seed>
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDAiFlMhBUKHIALzFpRVV1RENnrrenP6noZqTXravgcFhCzohGiyFEvTwIMIyAAegB+ZCHEDHd4hZardYQe4KMZ4IA)

----

```ts
declare class ApiFetcher<API> {
  fetch<Path extends keyof API>(path: Path): Promise<API[Path]>;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDMmp6ShH5D2KwsAAYqUV0JtqYxqEJWXl1Tvtgp3dfQNDI0eUxmcxmSyaKzWGy2Oz2DH4QA)

----

```ts
const fetcher = new ApiFetcher<SeedAPI>();
const berry = await fetcher.fetch('/seed/strawberry'); // OK
//    ^? const berry: Seed

fetcher.fetch('/seed/chicken');
//            ~~~~~~~~~~~~~~~
// Argument of type '"/seed/chicken"' is not assignable to type 'keyof SeedAPI'

const seed: Seed = await fetcher.fetch('/seeds');
//    ~~~~ Seed[] is not assignable to Seed
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDMmp6ShH5D2KwsAAYqUV0JtqYxqEJWXl1Tvtgp3dfQNDI0eUxmcxmSyaKzWGy2Oz2DH4CEKlGKt3K0GQAF4mBA-CNLjc3vcIlVJgsGIiQMiglBQpjkP44MBJK87lBYizyhMvLZOP5qaFNGTkNFkAB5ADSeBFhGQAD0APzIClU4IhIwKPB4DnQdmorm6bwVYAIfogQUMaUyq0ygB+dvtDsdUpiiigNCybHAyABYBCwhQmgARAbbEaTRAQIHNEQeiBRJI4GdgDRmAFnMgwKIM36A-1BsNiWpNJrlZIbKQ3NgsQymSjCWyOfrywYyc6rQ7K+YY0x4-Skym4GmUJnK3ggA)

----

```ts
declare function getDate(mon: string, day: number): Date;
getDate('dec', 25);
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDMmp6ShH5D2KwsAAYqUV0JtqYxqEJWXl1Tvtgp3dfQNDI0eUxmcxmSyaKzWGy2Oz2DH4hzSGWKOTyBSKNFKABEWhAJixChwqLRGpg4CEyCAsiwglBwTjIAxMWAGXjNIdNI0AEwAVgWDCAA)

----

```ts
declare function getDate(mon: string): (day: number) => Date;
getDate('dec')(25);
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPIxVADTIynBg5chCkCCY5MgA1hAhojDIVXgAfAAUwi3lZM2tAJRzUKIswHrVVSbz5WZjDMmp6ShH5D2KwsAAYqUV0JtqYxqEJWXl1Tvtgp3dfQNDI0eUxmcxmSyaKzWGy2Oz2DH4hzSGWKOTyBSKNFKABEWhAJixChwqLRwRNMHAQmQQFkWEEoAtkABeJ44yAMTFgVl4zSHTQLCYAJgArAsGEA)

----

```ts
declare function fetchAPI<API>():
  <Path extends keyof API>(path: Path) => Promise<API[Path]>;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPFUAfAAUAJQkjNXKcGDlyEKQIJjkyADWECGiMMj1DcKd5WQdXU3IALx1yMpQoizAerVqJgvlZnUMQA)

----

```ts
const berry = await fetchAPI<SeedAPI>()('/seed/strawberry'); // OK
//    ^? const berry: Seed

fetchAPI<SeedAPI>()('/seed/chicken');
//                  ~~~~~~~~~~~~~~~
// Argument of type '"/seed/chicken"' is not assignable to type 'keyof SeedAPI'
//
const seed: Seed = await fetchAPI<SeedAPI>()('/seeds');
//    ~~~~ Seed[] is not assignable to Seed
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPFUAfAAUAJQkjNXKcGDlyEKQIJjkyADWECGiMMj1DcKd5WQdXU3IALx1yMpQoizAerVqJgvlZnUMCIWUyEFQoSvI-nDAkiVllWrVEVNNDV62nP5XoU0TToyGiyAA8gBpPBgwjIAB6AH5kGcQBcASEjAo8HhnhUqu8FJ9vrpvBVgAgRiAgQxYXD6Qz6QA-FmstnsmExRRQGhZNjgZDjZBgELCFCaABEpNs5MpEBAEs0REGIFEkjg5HIwBozACzmFomFovFIzGEw+ak0nLwqIuNlIbmwyzufgeT1K+LeFtUjS+PwGNM5zNZjvMyqYarumu1uv1YENETwQA)

----

```ts
const fetchSeedAPI = fetchAPI<SeedAPI>();
const berry = await fetchSeedAPI('/seed/strawberry');
//    ^? const berry: Seed
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPFUAfAAUAJQkjNXKcGDlyEKQIJjkyADWECGiMMj1DcKd5WQdXU3IALx1yMpQoizAerVqJgvlZnUMCIWUxaUVEVUrl2WVatU3ao1Np+eSQVChd-5wwEkJQeL1UDS8tk4-m+oU07zw0UIhAAegB+ZBnEAXGEhIwKPBAA)

----

```ts
declare function apiFetcher<API>(): {
  fetch<Path extends keyof API>(path: Path): Promise<API[Path]>;
}

const fetcher = apiFetcher<SeedAPI>();
fetcher.fetch('/seed/strawberry');  // ok
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&module=7&target=4#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eJgQCI5wUCgwAK4gCGDAoiDIMBBgCAAWKqoAPFUAfAAUAJQkjNXKcGDlyEKQIJjkyADWECGiMMj1DcKd5WQdXU3IALx1yMpQoizAerVqJgvlZnUMyanpmTl5BUX2wABipRXQe6qNLRqEJWXl7bM9gj6A2Go3GkzUjRmXXmsw+Gy2OwgrwOs2ODH4eAQhUoxSe5WgK2Qd0ePxeESmTQY32eUFi1PKDS8tk4-iCUFCmkphGiyFEQzwQA)

----

```ts
function fetchAPI<API>() {
  type Routes = keyof API & string;  // local type alias

  return <Path extends Routes>(
    path: Path
  ): Promise<API[Path]> => fetch(path).then(r => r.json());
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMoQgE2QbwFDLLCYBcyAzmFKAOYDcByIcAthGZdSPXgL54QAHgAcA9lDBFw0eEjQZMAQQAKASVyMA5AHpyC8prLosAbQC6DQjr1ZtcYcIA2EQ-KyXk1hbqpwA7gBG0FAAnq7GmB7a2sgAdPF8eDAAriAIYMCiIMgwEGAIABYqqgA8xQB8ABQAlBqEYCHCKABKosmQ5MgAvMgA1hAhojDIxcgAZBRUtHSE0ciOoghwjsgNTcjLwHDkeIxQeclQ2SXKcGAFyEKQIJidre0Q5FWMhMJnBWSn54zVn1CiLGAejKahMXwKZnK3ShuXyBUqb3O1Vi5wgIEqUGhyCgsQAVuQsjVqgx+EA)

# Item 29: Prefer Types That Always Represent Valid States

## Things to Remember

- Types that represent both valid and invalid states are likely to lead to confusing and error-prone code.
- Prefer types that only represent valid states. Even if they are longer or harder to express, they will save you time and pain in the end!

## Code Samples

```ts
interface State {
  pageText: string;
  isLoading: boolean;
  error?: string;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5ABzgHMIAVCADzAC5kBnMKUEgbn2WAYBkB7OABNW9AEZ8+AGwhwQHAtCh8oAfnpMWIdrgC+uIA)

----

```ts
function renderPage(state: State) {
  if (state.error) {
    return `Error! Unable to load ${currentPage}: ${state.error}`;
  } else if (state.isLoading) {
    return `Loading ${currentPage}...`;
  }
  return `<h1>${currentPage}</h1>\n${state.pageText}`;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5ABzgHMIAVCADzAC5kBnMKUEgbn2WAYBkB7OABNW9AEZ8+AGwhwQHAtCh8oAfnpMWIdrgC+uQRASS4UFNLDIEAVyinwABVIR1zVhxhWQCMMD4hkdgZQjmQAFEyYzmgYkACUOJzAMMjhMRAAdIrK8XgEBKZgNv4ABgCitsoAhMgAqiBwotLIYHzIkgKCyAAk2Na2EA5OOvQ9EZCZFVA6xfLIOsgQkgwoSSljGdz8Qqw5nPkQhVAlW8Ja3b02dmAhEDrp9zOcevuHJQA8ABYAjAB8PX1XG46N4Aem+PwAOiBRml0sQyJQaNMOHogA)

----

```ts
async function changePage(state: State, newPage: string) {
  state.isLoading = true;
  try {
    const response = await fetch(getUrlForPage(newPage));
    if (!response.ok) {
      throw new Error(`Unable to load ${newPage}: ${response.statusText}`);
    }
    const text = await response.text();
    state.isLoading = false;
    state.pageText = text;
  } catch (e) {
    state.error = '' + e;
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMpjpZBvAUM5ABzgHMIAVCADzAC5kBnMKUEgbn2WAYBkB7OABNW9AEZ8+AGwhwQHAtCh8oAfnpMWIdrgC+uQRASS4UFNLDIEAVyinwABVIR1zVhxhWQCMMD4hkZGAAqlCSAGLKjmQAFIQumiQAlDjIpmA2-gDkmWzIenAMAJ5eyB5ePn6WABayZFEQ0UyYzmgYkAA0yCAQAO718azJeARNkAB03PxCrMgAvMjMVhDyC1CFOJwECH5MqRAMhDso83A9cMAWMBBgCFXRgSHhkU7R3X1OiYkrBMAwyNEAQlMByOYz4AGshpsCAsqkoel1esgAKK2ZTRAAGQRAcFE0gWfGQkgEgmQABJsG96jp6BTgYcQAwIGNRlYGJQaDoMV9oXoYZYdhZIDQ5shTucLPTQcKwNEefzRszJiSZvN4JImd9GG1mcQyByLPMZSsdJZMLd-hAoQqdWNFMpRdlkABqZDLTh6PRAA)

----

```ts
interface RequestPending {
  state: 'pending';
}
interface RequestError {
  state: 'error';
  error: string;
}
interface RequestSuccess {
  state: 'ok';
  pageText: string;
}
type RequestState = RequestPending | RequestError | RequestSuccess;

interface State {
  currentPage: string;
  requests: {[page: string]: RequestState};
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSgA)

----

```ts
function renderPage(state: State) {
  const {currentPage} = state;
  const requestState = state.requests[currentPage];
  switch (requestState.state) {
    case 'pending':
      return `Loading ${currentPage}...`;
    case 'error':
      return `Error! Unable to load ${currentPage}: ${requestState.error}`;
    case 'ok':
      return `<h1>${currentPage}</h1>\n${requestState.pageText}`;
  }
}

async function changePage(state: State, newPage: string) {
  state.requests[newPage] = {state: 'pending'};
  state.currentPage = newPage;
  try {
    const response = await fetch(getUrlForPage(newPage));
    if (!response.ok) {
      throw new Error(`Unable to load ${newPage}: ${response.statusText}`);
    }
    const pageText = await response.text();
    state.requests[newPage] = {state: 'ok', pageText};
  } catch (e) {
    state.requests[newPage] = {state: 'error', error: '' + e};
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyBEewORxO3240EeYSePmGW0gn26yAQJ3w1F6-XA0IgQjyGi04xRaLAEMyYARKHycIAdJNybg5pjJtihisibgAO7AMAIAAWyCe9M2nRpcKR6h6cFwKE4xV4bGYkvoEN+UFOAAMADJKOA8SgAEiozIGOKENItGqJUpl7GMBiVKpVPz+yA1VRUAEJkBcQHAAEbXFBgJTIa66kjII0m1lhISsI3C2SUmn2oRW5UIaWygKK5UTCBqzUAHj5AEYAHzRvoswZx4sAenLFYAOiBE1MsloaYsItEwOmiSIRDRpSkDsgQYdjqd+XBeBAcbDOqxKQAaZAgCCcnFvXgS7yipP4Rlbnds-FUOE6LikChsHbqWkxutUzfbnFE+IpLwq1EgdFJlwDg0TfOBOTgHlJ0LfknnOK47geZ4zxxd53mtZBgBgQVPSAkCAIgGkAgPJ1kDAPllE5d8qI9KAng1X0AyDMjQ3DPUoyoFChnjDi8NAsVsiwXBIhidN0OVEQnX-dFexE0l8nAyDST4giaUgGInnEp1aWPMBTw-C98ivFc-ECDdZP7R96DxLNeQFJ4IBIw9u10-TzzCFZL2vO1FBUNgN3tHQ2GQABqZBcSHYQaCAA)

----

```ts
interface CockpitControls {
  /** Angle of the left side stick in degrees, 0 = neutral, + = forward */
  leftSideStick: number;
  /** Angle of the right side stick in degrees, 0 = neutral, + = forward */
  rightSideStick: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqBJIA)

----

```ts
function getStickSetting(controls: CockpitControls) {
  return controls.leftSideStick;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqC7faHY6nc6x-xOCBgI68J4IE7xJRI1gQqEwuFFxG4T4on5-ZCFhEl3AAOlV0c1RyhSSAA)

----

```ts
function getStickSetting(controls: CockpitControls) {
  const {leftSideStick, rightSideStick} = controls;
  if (leftSideStick === 0) {
    return rightSideStick;
  }
  return leftSideStick;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqC7faHY6nc6x-xOCBgI68J4IE7xJRI1gQqEwuFFxG4T4owsgfDUVXRzVHKFcyNqjWZoR8hvFpGm4BEp4tnvt-x5XL5bl19QTHN-b7Ae3dmOT00iRe-KCnccb7VJIA)

----

```ts
function getStickSetting(controls: CockpitControls) {
  const {leftSideStick, rightSideStick} = controls;
  if (leftSideStick === 0) {
    return rightSideStick;
  } else if (rightSideStick === 0) {
    return leftSideStick;
  }
  // ???
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqC7faHY6nc6x-xOCBgI68J4IE7xJRI1gQqEwuFFxG4T4owsgfDUVXRzVHKFcyNqjWZoR8hvFpGm4BEp4tnvt-x5XL5bl19QTHN-b7Ae3dmOT019iBIlAj5BPLutzPT2fz+iL35QU7jjfarfqVGo5AAfjfwhoQA)

----

```ts
function getStickSetting(controls: CockpitControls) {
  const {leftSideStick, rightSideStick} = controls;
  if (leftSideStick === 0) {
    return rightSideStick;
  } else if (rightSideStick === 0) {
    return leftSideStick;
  }
  if (Math.abs(leftSideStick - rightSideStick) < 5) {
    return (leftSideStick + rightSideStick) / 2;
  }
  // ???
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqC7faHY6nc6x-xOCBgI68J4IE7xJRI1gQqEwuFFxG4T4owsgfDUVXRzVHKFcyNqjWZoR8hvFpGm4BEp4tnvt-x5XL5bl19QTHN-b7Ae3dmOT019iBIlAj5BPLutzPT2fz+iL35QU7jjfarfqfdPACyTBJADo4IbcGOIJTj5OyAALQrmuAHap8AA8yAAKznhePzLr+-4Tq6EpHqhUKfKiyAAEwPvQqI4QA-KRwg0EAA)

----

```ts
function getStickSetting(controls: CockpitControls) {
  return (controls.leftSideStick + controls.rightSideStick) / 2;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgEoQI4FcIGcwAKEIAJqAObIDeAUMsvnJAFzIDkADsWSOWwNw0AvjVCRYiFOmx4wAUShQA9lGp0GYJhFZtoyqAPV6VrfFAqCRY6PCRpMOfAGUsCJLlxr6jFuyUBrQ3oOOHIIABUIAA8wUzBzXksaMABPLnsZZ01IZABeDMdCbgpkAB8C2QV9MornV3dcQVFwG0lkJ2yUWnoELEViQlDtDQTyQXooB1lcVioAbRCwuNGAXVZpQo6tISSYLBAEMGAlEGQwsABVKAAbADEVAiGACg5ligBKamRJsD7TtgEyCsLQkdgAwkoEP4OMAwBDwMprp5usgAPQAKnRyAAgrxriglDBkGAABYofEwMAMYAkFD4YBQ5CgZC08iTPAAGmQAAY8sgQBAsPE4NcuQBqPkwFQAdzgUBIyHRqPUFLAThpEA6DP8rBAWAAtgAjaDjNGYnF4glE0koczkElU3AajTapmnVns3Bc3n5AVCqAi8WSmVyhVK9R2h3q2laqG6g3GqC7faHY6nc6x-xOCBgI68J4IE7xJRI1gQqEwuFFxG4T4on5-ZAF6sl3AAOlV0c1R0ZEsLCNbbcjao1mc+qOQACYkkA)

----

```ts
interface CockpitControls {
  /** Angle of the stick in degrees, 0 = neutral, + = forward */
  stickAngle: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHsEGsAOwwbhToA2AzsgN4BQyyA9AFSPICCIA5iSujMmAAsUZMMGzJQyACYQOUCBDIAaZAAZkAXmQgIAVzBQ4JFQGpNyGOigB3OFCnJG9WshFis7LhABc23QFsAI2gAbmoAX2ogA)


# Item 30: Be Liberal in What You Accept and Strict in What You Produce

## Things to Remember

- Input types tend to be broader than output types. Optional properties and union types are more common in parameter types than return types.
- Avoid broad return types since these will be awkward for clients to use.
- To reuse types between parameters and return types, introduce a canonical form (for return types) and a looser form (for parameters).
- Use `Iterable<T>` instead of `T[]` if you only need to iterate over your function parameter.

## Code Samples

```ts
declare function setCamera(camera: CameraOptions): void;
declare function viewportForBounds(bounds: LngLatBounds): CameraOptions;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMJwLbTgeQA5jAD2IAzsgN4BQyyS40A-AFzIAyIA5m3GANw1kALyJEMLZCACuGAEbQBteXCihOE6XIWC8wMAgAWGmfKgCAvlTABPPCg7deyALyCKyADZdWm030+8PiYKyObIAD5uniRBWmYBYLF+oRGCANq+0AA0ksFQALoCNnbsXDxgAEJEUiAAJuSutBQgRFBgBhBwpImljmA5pNXtAO4Q3awO5WGRtGmTvDnzYPmps5lQOeubedtxhVS1EAgeKigwNQiEJMikEGDoWFBwABQImNisD9j4V2QAlKwAG5EYC1ASHY6nZDnECXYggZCA4AQYZ4VpgABirSqNXqz1k1TqpAmZV4OKJALQ7yeP3hpAEQA)

----

```ts
interface CameraOptions {
  center?: LngLat;
  zoom?: number;
  bearing?: number;
  pitch?: number;
}
type LngLat =
  { lng: number; lat: number; } |
  { lon: number; lat: number; } |
  [number, number];
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMJwLbTgeQA5jAD2IAzsgN4BQyyS40A-AFzIAyIA5m3GANw1kALyJEMLZCACuGAEbQBteXCihOE6XIWC8wMAgAWGmfKgCAvlTABPPCg7deyALyCKyADZdWm030+8PiYKyObIAD5uniRBWmYBYLF+oRGCANq+0AA0ksFQALoCQA)

----

```ts
type LngLatBounds =
  {northeast: LngLat, southwest: LngLat} |
  [LngLat, LngLat] |
  [number, number, number, number];
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMJwLbTgeQA5jAD2IAzsgN4BQyyS40A-AFzIAyIA5m3GANw1kALyJEMLZCACuGAEbQBteXCihOE6XIWC8wMAgAWGmfKgCAvlTABPPCg7deyALyCKyADZdWm030+8PiYKyObIAD5uniRBWmYBYLF+oRGCANq+0AA0ksFQALoCNnbsXDxgAEJEUiAAJuSutBQgRFBgBhBwpImljmA5pNXtAO4Q3awO5WGRtGmTvDnzYPmps5lQOeubedtxhVRAA)

----

```ts
function focusOnFeature(f: Feature) {
  const bounds = calculateBoundingBox(f); // helper function
  const camera = viewportForBounds(bounds);
  setCamera(camera);
  const {center: {lat, lng}, zoom} = camera;
               // ~~~      Property 'lat' does not exist on type ...
               //      ~~~ Property 'lng' does not exist on type ...
  zoom;
  // ^? const zoom: number | undefined
  window.location.search = `?v=@${lat},${lng}z${zoom}`;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMJwLbTgeQA5jAD2IAzsgN4BQyyS40A-AFzIAyIA5m3GANw1kALyJEMLZCACuGAEbQBteXCihOE6XIWC8wMAgAWGmfKgCAvlTABPPCg7deyALyCKyADZdWm030+8PiYKyObIAD5uniRBWmYBYLF+oRGCANq+0AA0ksFQALoCNnbsXDxgAEJEUiAAJuSutBQgRFBgBhBwpImljmA5pNXtAO4Q3awO5WGRtGmTvDnzYPmps5lQOeubedtxhVS1EAgeKigwNQiEJMikEGDoWFBwABQImNisD9j4V2QAlKwAG5EYC1ASHY6nZDnECXYggZCA4AQYZ4VpgABirSqNXqz1k1TqpAmZV4OKJALQ7yeP3hpCKthQGM6YCkUBQzmQcBA1nBRxO7OhF1+dDgHgQUhOkHJtTUVQAHs8YKxmbw2RBKRkdrk4rtTHroPsYXDrjAiBLSDgQKrWeylSqWeq-pRBAgSN1kATcQ1ReLJbwIDK5URFTA-v4APQR5AdDx2KBC2G-V3usCix5wFyI5Go9FYqAy0j4wn1cOCW73akvN4Zsu0N1kNMUeiQKCsChSnJeTjmHIiMRhTk17CKWhj8cTqPIAB+s4nyAAClAiPGbMgAORS9fIWpEMaSIhpiDy4Ae67FFAAOmvgnnd6nE9n08Xy9X1g33e3u-3LSPJ7PCIXsg16XoI-YYKOU4AHqMHQqbCKIGBJNAETILiEAwKAEC1IIwygLuwyXh45q8PCl63CohhZgABowgLOAAAgAJB2vC9ix3bmEILHgeY1EWFQQA)

----

```ts
interface LngLat { lng: number; lat: number; };
type LngLatLike = LngLat | { lon: number; lat: number; } | [number, number];

interface Camera {
  center: LngLat;
  zoom: number;
  bearing: number;
  pitch: number;
}
interface CameraOptions extends Omit<Partial<Camera>, 'center'> {
  center?: LngLatLike;
}
type LngLatBounds =
  {northeast: LngLatLike, southwest: LngLatLike} |
  [LngLatLike, LngLatLike] |
  [number, number, number, number];

declare function setCamera(camera: CameraOptions): void;
declare function viewportForBounds(bounds: LngLatBounds): Camera;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgDIgOarmZBvZAG0wC5kQBXAWwCNoBuInMy2h5AX3oCgwBPAA4p0WHKmABrFAF40mbLgA++IgHsQLanSiNCzclvYdkygNqttAGgNsoAXR7dQkWIhQBhOFWhx83ZMhI4NBkIgo8AQBeqqpUmrYRyHRwUKAY8dqJAsBgCAAWGQzcHE7BrkjInt5QcADyAmDA6gDOyBAAHpAgACattVQ5ADwACimNcISDVT4AfNYA5EEu8zN+AUvQAPyh8mKSEDwl-EJyomAAQqoUPa3S-vggqlBgeRBwzWA7Z+JS1s1XLwA7hAPl8FD8IMZFPdTGE9r9TuD9nYTDCLNBrOioJjDNibNoHNxuN0IAg9FAUDBrghGupkM0IGBpjUABQILw+MjMuoNJogZoASjIADdVMBujwSWSUpTqbSQMhhcAIICBE8wAAxJ6Xa69Fk0K43ME4HU3IWVDk1HhAA)

----

```ts
interface CameraOptions {
  center?: LngLatLike;
  zoom?: number;
  bearing?: number;
  pitch?: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgDIgOarmZBvZAG0wC5kQBXAWwCNoBuInMy2h5AX3oCgwBPAA4p0WHKmABrFAF40mbLgA++IgHsQLanSiNCzclvYdkygNqttAGgNsoAXR6hIsRCgDCcKtDgB5AWGB1AGd8bmRkJHBoAH4yEQVxKR5wgC9VVSpYm21k5Do4KFAMLIsGMOQBYDAEAAsSwx1uDm4gA)

----

```ts
function focusOnFeature(f: Feature) {
  const bounds = calculateBoundingBox(f);
  const camera = viewportForBounds(bounds);
  setCamera(camera);
  const {center: {lat, lng}, zoom} = camera;  // OK
  //                         ^? const zoom: number
  window.location.search = `?v=@${lat},${lng}z${zoom}`;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAYhCGwCuAnaBeK8B2IDcAUACYQDGANvGlAGZLanACWA9tlKfOaUpcBACEW9Ik2wBzIQA8AFDQBcsBMjQBKRQG1sSALYAjCCgA0UbfsMmzB46d3WAuoTH8UNeKWgAZCZ8RQA3lDkEopWhnhBiKF24VAAvoSgkFDe4r7AnkwA1hgpPn4APgFBbNHmKBF8ZdYRcVBFWjE2YSiOBATOhm4eUADC8DqG8AEEUBwQ2C6KqemEYwBeLCw61eGjUAZUYuKrFetgTMCkABa7hHEdk13u0P2DKPAA8mDMbADOUBBS-NhEH486Q4AHgAClRmFwgXchgA+EwAcg8VxQ8JhIzGSJcAH5pvkMtkIOcCEkvHihCIPuh1v5sCwUMBjgg3sBcWlEJkciY3sIGQB3CDM1npDkQOoFdYaGbsgkmKX4nL2eoSlqWJqq8rqhyEYhkSjUOgMV7sN4QYDQh4yTj3eCKc1PF6sbBvdRQABuLCYREIJAoVGgBsYjrdTAgvLAdOAMDp5N+bxkemEsaFiBjfxddsIAaNtBYPDej2wcEQqAgckURZUEFU6I472AG0TfygmE43F4iEEje20jkqjmtad9atQ2bwdD4fpUZQqbjCYpffWJrNAyGlpXDwXGLrAUxhkU-j4JmC4jiJkWyzqLfX8AiUAA9HeoI8ANLrB9jD+fr-fr8APSxA7MlA54rLY5TrLyYhECwvIAHTkLmiCOrBJpUCco4AAZYq66AAAIACQHogp6EcecTzIRIFxBhRJAA)

----

```ts
function sum(xs: number[]): number {
  let sum = 0;
  for (const x of xs) {
    sum += x;
  }
  return sum;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZxAWwBQA9kC5FjoBGApgE4DaAugJT6FqlmIDeAUIogDYlQrqIAvIgAMAbg6JgcZhggJkfLIjjBEOGq0mdUaRAGphWCZwC+ksrxBkkuieaA)

----

```ts
function sum(xs: Iterable<number>): number {
  let sum = 0;
  for (const x of xs) {
    sum += x;
  }
  return sum;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZxAWwBQA9kC5ECSUApgE4CGARgDbEA8Y6lZAfAJT6NrOmIDeAKESJaUFOkQBeRAAYA3EMTA4vDBATIxWRHGCIcbfouGo0iANTSsC4QF9FpYlBCkkphfaA)

----

```ts
const six = sum([1, 2, 3]);
//    ^? const six: number
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZxAWwBQA9kC5ECSUApgE4CGARgDbEA8Y6lZAfAJT6NrOmIDeAKESJaUFOkQBeRAAYA3EMTA4vDBATIxWRHGCIcbfouGo0iANTSsC4QF9FpYlBCkkphffVhNKGNummGADaAIwANIgATBEAzAC6bAoA9EnCwgB6APyIXj7IfpxMZAJAA)

----

```ts
function* range(limit: number) {
  for (let i = 0; i < limit; i++) {
    yield i;
  }
}
const zeroToNine = range(10);
//    ^? const zeroToNine: Generator<number, void, unknown>
const fortyFive = sum(zeroToNine);  // ok, result is 45
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZxAWwBQA9kC5ECSUApgE4CGARgDbEA8Y6lZAfAJT6NrOmIDeAKESJaUFOkQBeRAAYA3EMTA4vDBATIxWRHGCIcbfouGo0iANTSsC4QF9FpYlBCkkphfdCRYCAFSIKMABzYgxqGDQYKE4mMkNBYWVVUUQYKVk5VMQ6EQiozJhzc3jjRABPGGJqABNUm0R7e3UwTUQALzI4ABU4ADkYMGJ0wJCMAEYZNgUAemnhYQA9AH5EZtaO0m6+geJ8AHFiQYooFQZY0gAaRAA3OBhqq-AAazA4AHcwFgE1sSSoMoAYjBrkNpKYMBstv1BlNhLMdE8ro5UNQxDBkIgACwAVgEQA)


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


# Item 32: Avoid Including null or undefined in Type Aliases

## Things to Remember

- Avoid defining type aliases that include `null` or `undefined`.

## Code Samples

```ts
function getCommentsForUser(comments: readonly Comment[], user: User) {
  return comments.filter(comment => comment.userId === user?.id);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHsC2mLmQb2QFcBnaASQBMAuZEsKUAcwG5kBfAKFElkRQCqZKAWTAadBszZcYREAjDB0IZEwhgM2XGBIAxdFCHQAFAiw5wJWlAhxKKgDYBPNBZ0BtALoAaYsNpjKABKAk5kZFswIihVc20rADoYYEdeM3c8AF4APmR4yzBE0gpKZCyK-2gAfkTxYJZOLiA)

----

```ts
type User = { id: string; name: string; } | null;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgzhATlAvFA3lAlgEwFxRzCJYB2A5gNxSkCGAthAUSRdQL5QA+NArgDb9KAKCA)

----

```ts
interface User {
  id: string;
  name: string;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgKoGdrIN4ChnLAAmAXMumFKAOYDc+yIcAthGRVSHbgL65A)

----

```ts
type NullableUser = { id: string; name: string; } | null;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAcgrgGwQQwEYIgVQM4QE5QC8UA3lAJYAmAXFNsHuQHYDmA3FE8gLYS32NWHAL5QAPp0QI2AKCA)

----

```ts
function getCommentsForUser(comments: readonly Comment[], user: User | null) {
  return comments.filter(comment => comment.userId === user?.id);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHsC2mLmQb2QFcBnaASQBMAuZEsKUAcwG5kBfAKFElkRQCqZKAWTAadBszZcYREAjDB0IZEwhgM2XGBIAxdFCHQAFAiw5wJWlAhxKKgDYBPNBZ0BtALoAaYsNpjEQAfZBAiR0cASgJOZGRbMCIoVXNtKwA6GGBHXjN3PABeAD5kNMswDNIKSmRC+v9oAH4M8SiWTi4gA)

----

```ts
type BirthdayMap = {
  [name: string]: Date | undefined;
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHsC2mLmQb2QFcBnaASQBMAuZEsKUAcwG5kBfAKFElkRQCqZKAWTAadBszZcwATwAOKAELAoYABaU4cgLJwFyALwFOyZAG0QcHLXqMQTALq0AInEjIAPsRCUIMKAQlCyc7KFAA)

----

```ts
type BirthdayMap = {
  [name: string]: Date | undefined;
} | null;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgMIHsC2mLmQb2QFcBnaASQBMAuZEsKUAcwG5kBfAKFElkRQCqZKAWTAadBszZcwATwAOKAELAoYABaU4cgLJwFyALwFOyZAG0QcHLXqMQTALq0AInEjIAPsRCUIMKAQlCyc7N7IIEQANtGhQA)


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


# Item 34: Prefer Unions of Interfaces to Interfaces with Unions

## Things to Remember

- Interfaces with multiple properties that are union types are often a mistake because they obscure the relationships between these properties.
- Unions of interfaces are more precise and can be understood by TypeScript.
- Use tagged unions to facilitate control flow analysis. Because they are so well supported, this pattern is ubiquitous in TypeScript code.
- Consider whether multiple optional properties could be grouped to more accurately model your data.

## Code Samples

```ts
interface Layer {
  layout: FillLayout | LineLayout | PointLayout;
  paint: FillPaint | LinePaint | PointPaint;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBUAsFMGdtAO2tAJqALge1AIwQJaIDGWAtgA4CGGBuANggGSimWMAeo0iWArgHNImHLwygB0cUXpE0oItwBOSrEtBk4sKpNgA6AFAYAnhQQAxAvXoAFKkXEBeUAG9L1uw4BcoAOS+AXwBuI1MEABk5T0QnV0jkaIwff2DQs1AbLAdE0GcXTOz7GOTAkJN093pwqmN+WLcrKpq6ktTyiLlq2r56+Ogulr9StIQCmIGe3NcxjAmkodSHaCUAMypiCJrl1wNQUHpmnp9KudAAH1A+04uZuZC96m9QSpyLvteMrJjEkICDIA)

----

```ts
interface FillLayer {
  layout: FillLayout;
  paint: FillPaint;
}
interface LineLayer {
  layout: LineLayout;
  paint: LinePaint;
}
interface PointLayer {
  layout: PointLayout;
  paint: PointPaint;
}
type Layer = FillLayer | LineLayer | PointLayer;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBUAsFMGdtAO2tAJqALge1AIwQJaIDGWAtgA4CGGBuANggGSimWMAeo0iWArgHNImHLwygB0cUXpE0oItwBOSrEtBk4sKpNgA6AFAYAnhQQAxAvXoAFKkXEBeUAG9L1uw4BcoAOS+AXwBuI1MEABk5T0QnV0jkaIwff2DQs1AbLAdE0GcXTOz7GOTAkJN093pwqmN+WLcrKpq6ktTyiLlq2r56+Ogulr9StIQCmIGe3NcxjAmkodSHaCUAMypiC0au5dcDUFB6Zp6fSrmQ-epvUErEkICDJdX1juRt9Rc9g6P5vrPPy+KoD6twM90eaw2GSy4xqOw++0O3XmMz+FyKyOhGBB93aQNh6mcp3xoAAPkDOsSySj8SEgA)

----

```ts
interface Layer {
  type: 'fill' | 'line' | 'point';
  layout: FillLayout | LineLayout | PointLayout;
  paint: FillPaint | LinePaint | PointPaint;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBUAsFMGdtAO2tAJqALge1AIwQJaIDGWAtgA4CGGBuANggGSimWMAeo0iWArgHNImHLwygB0cUXpE0oItwBOSrEtBk4sKpNgA6AFAYAnhQQAxAvXoAFKkXEBeUAG9L1uw4BcoAOS+AXwBuI1MEABk5T0QnV0jkaIwff2DQs1AbLAdE0GcXTOz7GOTAkJN093pwqmN+WLcrKpq6ktTyiLlq2r56+Ogulr9StIQCmIGe3NcxjAmkodSHaCUAMypiCJrl1wNQTDDklcbfUAAfP1lkE-PfCiyY3xC9+maen0q5s9A+z-OZuaeoGo3lAlRy5z64Iy9wwiRCAQMQA)

----

```ts
interface FillLayer {
  type: 'fill';
  layout: FillLayout;
  paint: FillPaint;
}
interface LineLayer {
  type: 'line';
  layout: LineLayout;
  paint: LinePaint;
}
interface PointLayer {
  type: 'paint';
  layout: PointLayout;
  paint: PointPaint;
}
type Layer = FillLayer | LineLayer | PointLayer;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBUAsFMGdtAO2tAJqALge1AIwQJaIDGWAtgA4CGGBuANggGSimWMAeo0iWArgHNImHLwygB0cUXpE0oItwBOSrEtBk4sKpNgA6AFAYAnhQQAxAvXoAFKkXEBeUAG9L1uw4BcoAOS+AXwBuI1MEABk5T0QnV0jkaIwff2DQs1AbLAdE0GcXTOz7GOTAkJN093pwqmN+WLcrKpq6ktTyiLlq2r56+Ogulr9StIQCmIGe3NcxjAmkodSHaCUAMypiC0au5dcDUEww5JXG3xD9+maen0q5s9Bqb1BKxJCAgyXV9Y7kbfUXPYOZmSsmQpwBF268z6twBD2KoD6LwMbw+aw2GSy4xqO3++3ayThGDB50u8xmMP2hJ8MyRb3aCOx6mcN0ZoAAPgjOqyOeTGSEgA)

----

```ts
function drawLayer(layer: Layer) {
  if (layer.type === 'fill') {
    const {paint} = layer;
    //     ^? const paint: FillPaint
    const {layout} = layer;
    //     ^? const layout: FillLayout
  } else if (layer.type === 'line') {
    const {paint} = layer;
    //     ^? const paint: LinePaint
    const {layout} = layer;
    //     ^? const layout: LineLayout
  } else {
    const {paint} = layer;
    //     ^? const paint: PointPaint
    const {layout} = layer;
    //     ^? const layout: PointLayout
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PTAEBUAsFMGdtAO2tAJqALge1AIwQJaIDGWAtgA4CGGBuANggGSimWMAeo0iWArgHNImHLwygB0cUXpE0oItwBOSrEtBk4sKpNgA6AFAYAnhQQAxAvXoAFKkXEBeUAG9L1uw4BcoAOS+AXwBuI1MEABk5T0QnV0jkaIwff2DQs1AbLAdE0GcXTOz7GOTAkJN093pwqmN+WLcrKpq6ktTyiLlq2r56+Ogulr9StIQCmIGe3NcxjAmkodSHaCUAMypiC0au5dcDUEww5JXG3xD9+maen0q5s9Bqb1BKxJCAgyXV9Y7kbfUXPYOZmSsmQpwBF268z6twBD2KoD6LwMbw+aw2GSy4xqO3++3ayThGDB50u8xmMP2hJ8MyRb3aCOx6mcN0ZoAAPgjOqyOeTGSEVnwSLQsIhQKglFQAO6-AAUEOWPl+AEpdvsCCtQHLGXp6Y49X5jtZfCrcftWCLYOIXISAlN5Uo7vsQGb9gA9AD85sQlvuRXmzz9AP2pG9VohdVtzntjtAzpdHq9PvDVyeW1JANt0Ho8AUGq1xmWOrCuX1vhB0GNqrNIZ91r9kdA0aDsbA8c9NfEVM5CUDLo7rmTGAbTZdcbNCf7g8VXMhGe42YQpuDFqtNrtfObY7d7ZXvseNN71d3LkHw43o9b453ocbpOpmNm6f2bzeQA)

----

```ts
interface Person {
  name: string;
  // These will either both be present or not be present
  placeOfBirth?: string;
  dateOfBirth?: Date;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyIcAthAFzIZhSgDmA3EcgPRvIAqAFhBigDuwADYjkEYGD5RkAIyzT5KAA5R+EcMiyyQi5cjUbwrFSMQQA8jABCwKNID81WvRDNWAEziRrdhzzOyAAiPhAsAL4EQA)

----

```ts
interface Person {
  name: string;
  birth?: {
    place: string;
    date: Date;
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyIcAthAFzIZhSgDmA3EcgEbBRgAWA-NYWLEADgBtEVGnUYshyACZxI1ACJKIs5AF8COoA)

----

```ts
const alanT: Person = {
  name: 'Alan Turing',
  birth: {
// ~~~~ Property 'date' is missing in type
//      '{ place: string; }' but required in type
//      '{ place: string; date: Date; }'
    place: 'London'
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyIcAthAFzIZhSgDmA3EcgEbBRgAWA-NYWLEADgBtEVGnUYshyACZxI1ACJKIs5AF8COhDlrI44kABVq6KNlwBefK1IVqAcgCCJ5KYCu9EA2cANKwcXNwCBAD0EcgAfnExaFBYwtBgAJ7IzoqQzsjAGMhk+RiMebjpKZHRcpl4yGIS1LS+zNq5bF5gyFAQAI5enBDyZcgVEFU1tfXiSE3SfkwK6qrqi1rOrCIzks4AMjjyOBvEOjpAA)

----

```ts
function eulogize(person: Person) {
  console.log(person.name);
  const {birth} = person;
  if (birth) {
    console.log(`was born on ${birth.date} in ${birth.place}.`);
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyyIcAthAFzIZhSgDmA3EcgEbBRgAWA-NYWLEADgBtEVGnUYshyACZxI1ACJKIs5AF8COmAFcQCMMBzII+0VgbAAXhAAUwzDmroo2EAEp8rBDmxRCAA6KwYnFxBg0govTX8QWnwOLm4tZABeZGcPHE1gGGQHFJ4fQSEEwJCwhwADAHc4DHYsKFwzABI8Eu5gxUh00GQunuCxCS1g2rjWHR0gA)

----

```ts
interface Name {
  name: string;
}

interface PersonWithBirth extends Name {
  placeOfBirth: string;
  dateOfBirth: Date;
}

type Person = Name | PersonWithBirth;
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgHJwLYoN4ChnIiYQBcyAzmFKAOYDcuAvrrqJLIigArTkD2IAOrAwACwBCwKGOQQAHpBAATcmmLI8BAA4AbTgHkYk6aLKVqIevmRK4kQ8bFkAInYgNmuMAE8t3XgLIALxqWMgAPsg8UPxCIhJSYgxAA)

----

```ts
function eulogize(person: Person) {
  if ('placeOfBirth' in person) {
    person
    // ^? (parameter) person: PersonWithBirth
    const {dateOfBirth} = person;  // OK
    //     ^? const dateOfBirth: Date
  }
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgHJwLYoN4ChnIiYQBcyAzmFKAOYDcuAvrrqJLIigArTkD2IAOrAwACwBCwKGOQQAHpBAATcmmLI8BAA4AbTgHkYk6aLKVqIevmRK4kQ8bFkAInYgNmuMAE8t3XgLIALxqWMgAPsg8UPxCIhJSYgwwAK4gCGDAgRApOnw0wABeEAAUfjECZNGxAJQa1sAwyCUA5LoGRomiLcigyOW19QTaASDWBAD0E8gAegD8zVpwUMTsdQOVUaPCYo6i48gIApQatvadJozB-aN0k9P6ANIHU8ME84fHYDZuDl0ubmszGYQA)


# Item 35: Prefer More Precise Alternatives to String Types

## Things to Remember

- Avoid "stringly typed" code. Prefer more appropriate types where not every `string` is a possibility.
- Prefer a union of string literal types to `string` if that more accurately describes the domain of a variable. You'll get stricter type checking and improve the development experience.
- Prefer `keyof T` to `string` for function parameters that are expected to be properties of an object.

## Code Samples

```ts
interface Album {
  artist: string;
  title: string;
  releaseDate: string;  // YYYY-MM-DD
  recordingType: string;  // E.g., "live" or "studio"
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgIIBsBGBXAtsgbwChlk4oxgBnMALmRqlAHMBuE5SsdCexl9qSgQecKhAAicSHzBMQbUgHolyAJoa1AWgCyOrRIkdhCAPZQAJiwAqATwAOvBnIHLVAUQB0zTwBpkAETowABuEAHI5oE02FamAUQAvkRAA)

----

```ts
const kindOfBlue: Album = {
  artist: 'Miles Davis',
  title: 'Kind of Blue',
  releaseDate: 'August 17th, 1959',  // Oops!
  recordingType: 'Studio',  // Oops!
};  // OK
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgIIBsBGBXAtsgbwChlk4oxgBnMALmRqlAHMBuE5SsdCexl9qSgQecKhAAicSHzBMQbUgHolyAJoa1AWgCyOrRIkdhCAPZQAJiwAqATwAOvBnIHLVAUQB0zTwBpkAETowABuEAHI5oE02FamAUQAvkRmIDTIANagFgDyMABC6NhOGDj4ALyEHOSUNPQA5DrAPFTIUiHU9b4cXDwNANLZkTDIhcVdxiIQYpLSTvWo2MzY6QCMAOxgABb+qwCcAKx7XW7IOab2VACEk2aWNg7zAMpgscCmJ8gqZxfXSaynHL9IhAA)

----

```ts
function recordRelease(title: string, date: string) { /* ... */ }
recordRelease(kindOfBlue.releaseDate, kindOfBlue.title);  // OK, should be error
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgIIBsBGBXAtsgbwChlk4oxgBnMALmRqlAHMBuE5SsdCexl9qSgQecKhAAicSHzBMQbUgHolyAJoa1AWgCyOrRIkdhCAPZQAJiwAqATwAOvBnIHLVAUQB0zTwBpkAETowABuEAHI5oE02FamAUQAvkRmIDTIANagFgDyMABC6NhOGDj4ALyEHOSUNPQA5DrAPFTIUiHU9b4cXDwNANLZkTDIhcVdxiIQYpLSTvWo2MzY6QCMAOxgABb+qwCcAKx7XW7IOab2VACEk2aWNg7zAMpgscCmJ8gqZxfXSaynHL9IgwbAgBCUUwgZAmcwWABKUxmAApek5+Ap-BY5rJ5MwAJSEL4AKmQnnJyGJqmSsMsiNE4mRWRAuQKRQgnmEDNmkH8zNZYw5aPxAK+qiB-ioW1M2HQFmQmBQ0Cg5iIQA)

----

```ts
type RecordingType = 'studio' | 'live';

interface Album {
  artist: string;
  title: string;
  releaseDate: Date;
  recordingType: RecordingType;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7cQA)

----

```ts
const kindOfBlue: Album = {
  artist: 'Miles Davis',
  title: 'Kind of Blue',
  releaseDate: new Date('1959-08-17'),
  recordingType: 'Studio'
// ~~~~~~~~~~~~ Type '"Studio"' is not assignable to type 'RecordingType'
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7cSJgUUADWWKgA8kIAQkyUFlBSsgrEyqrqmjqkALLo5mRQrqxaJAA0KlCm5rokANLJUIhCUJnZTS12Dk6eOZgQAO61bhAAFCQAjACcAKyrALQADAAcW8sA7CQAlM2qPiiheAQdAMpUNCTcAPSvUAB+3z+-31DhUgAIke1HQiCBdC0UEwiGAajIZHQ2EwImk5laiFaBFIwWu-gIL0iPCAA)

----

```ts
function getAlbumsOfType(recordingType: string): Album[] {
  // ...
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7cQpSY8JqImFDYEMBSsnJkAPJC4QAUPiiheASWwAY4AJS6GfIA2gC6SipQAPRtUADC2QCyAAowAKIAyiOtdlTIyU02HVBDAHLO3NHcQA)

----

```ts
/** What type of environment was this recording made in? */
type RecordingType = 'live' | 'studio';
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/PQKhAIHUAsEMBdzwJ4AcCm4D2Azc6A7ANwEsAnLAgW0MQHdYBnJaE5s9AYyzIBMSCAc3BVYvTAID84EMABQKDOABKXHvyEAVNJgC84AOQAbEkXQHwAH0ON4AV35YDAbjlA)

----

```js
function pluck(records, key) {
  return records.map(r => r[key]);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwDYggawBQCcCmEcuAJgM4A0im+AngJSIDeAUIogVCLkgUaWQB0AWwCGyPIgC8APg4BtGrQC69ANwsAviyA)

----

```ts
function pluck(records: any[], key: string): any[] {
  return records.map(r => r[key]);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwDYggawBQCcCmEcuAJgM4BciAhmAJ4DaAugDSKb51VlS4xgBzAJRVajJogDeAKESICUELiQEipMgDoAttWR5EAXgB88hhzpMhAbmkBfaUA)

----

```ts
function pluck<T>(records: T[], key: string): any[] {
  return records.map(r => r[key]);
  //                      ~~~~~~ Element implicitly has an 'any' type
  //                             because type '{}' has no index signature
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwDYggawDwBUB8AFAE4CmEcxAJgM4BciuA2gLoA0impAngzVMRhgA5gEoGAQzDdWiAN4AoRIjJQQxJGQrUaAOgC2E5CUQBefCqZduLUQG4liAPRPlb9x8-KAfr7+IAUVRSfVIwKEQYfTQYCBgoVG5EAAsJGkQpRAByKW4sxChuZFJHFy9yio8AI3IJEBpSAqLGrLkAX3zU9LA4SLAqUgAPRBoYYTAJNTIFNoUgA)

----

```ts
type K = keyof Album;
//   ^? type K = keyof Album
//      (equivalent to "artist" | "title" | "releaseDate" | "recordingType")
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7coJBQANJQxADWECCIQlBSsnI8APR5qlAAegD8ULHQiSlpGVky8jEEsBBkiEzsADwwIgDuAHxJsH1QEAAeApioZFAAYpSY8JqImFDlPb1QuooA2olYUKnpmRsAukF9e6eRPJVQAMogmMAAFtUtbR0QnfH9+YWqMoVZqPZ5vIYAInUmgoEIYUAhpnMcMYELsDicnggKIRPhQoTwBAhvCAA)

----

```ts
function pluck<T>(records: T[], key: keyof T) {
  return records.map(r => r[key]);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7cQpSY8JqImFBgTJTwANYAPLgAfAAUPiioZLq4ANoAugA0UBkQILr1IIhCULgAlEoqthBUyMlFaGQAdHIiYIVQhLm25c2VHVHcQA)

----

```ts
const releaseDates = pluck(albums, 'releaseDate');
//    ^? const releaseDates: (string | Date)[]
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAShDGB7ATgEwJYDsDmAVc0AvFAOQDOwArhoiVAD6kA26AbhCQNwBQ3WwEZADMAhvGgBBJgCNKAWygBvblCgjkwdBQBcUCsizYeqzcCYRd+w8ajII5kWQgAREQN2uBNu0jSH8kLpwvhg4ARA8AL7cQpSY8JqImFBgTJTwANYAPLgAfAAUPiioZLq4ANoAugA0UBkQILr1IIhCULgAlEoqthBUyMlFaGQAdHIiYIVQhLm25c2VHVHcqAhM6tDmwGoy8qVQUrJyVTxImBS9Dk6eEGTTKWmZ+SK7cmS1JHZXLm4cS9wAegBqlUAD0APxQM4XL4QRw-AT7fJWHAMKA3DpVbhAA)

----

```ts
function pluck<T, K extends keyof T>(records: T[], key: K): T[K][] {
  return records.map(r => r[key]);
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwDYggawDwBUA0iA0ogKYAeUpYAJgM6KakCecwiuAfABQBOpEOL3oAuDgG0AuoSbMxRAJRjc4opKmIA3gChEiflBC8k-QcLoA6ALYBDZH0QBeTvvGzJCgNzaAvtqA)

----

```ts
const dates = pluck(albums, 'releaseDate');
//    ^? const dates: Date[]
const artists = pluck(albums, 'artist');
//    ^? const artists: string[]
const types = pluck(albums, 'recordingType');
//    ^? const types: RecordingType[]
const mix = pluck(albums, Math.random() < 0.5 ? 'releaseDate' : 'artist');
//    ^? const mix: (string | Date)[]
const badDates = pluck(albums, 'recordingDate');
//                             ~~~~~~~~~~~~~~~
// Argument of type '"recordingDate"' is not assignable to parameter of type ...
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABABwDYggawDwBUA0iA0ogKYAeUpYAJgM6KakCecwiuAfABQBOpEOL3oAuDgG0AuoSbMxRAJRjc4opKmIA3gChEiflBC8k-QcLoA6ALYBDZH0QBeTvvGzJCgNzaAvtqjMyKSIAEoCQjQwYADmuIHBjogA5HSGkXBJiAA+yagwAG6kSd7aUVS8wDYQwQCCqABGIFZauog2vLCpYqm8UdHeerBQqKTdUL0xA-qkIzZ0pAAiNlRiS1RTphF9cUFiYWaRMTuk3n40AqjtwSNQbQ1NdGJ1jVZS3oJgqYg0y6QMiWgMJhuDZ7lY6IQkvxZvM1kUvNoAPSIvR6AB6AH5EB8vj8qI9EHCpNocbd2p0oP8UOgsCCwRDkuSYKkkgjkajEJjsQgvkzUgSen1iaTEAEglTAbTQS8GVDwsJtvFWd52aiuSKxX89vLDrF4sKebcrDByE5qUC6TLCABZZYACwsvBstDgVm4CkQ2EQAAYLABWRBYuUwxa-TJiJJ8qDKpEotVYkXG8hibiCmLZQm-BQGz63eo2GhwiU04HSh6QzYKmJwmOqjn1huN+sAP1bbfbHdjiBqvGiTWotzYoviyQARJXdXDR5lmYgwHAyXQ6DBomAbPURqK4Ch2jYrKRyogh5rEBYz9ogA)


# Item 36: Use a Distinct Type for Special Values

## Things to Remember

- Avoid special values that are assignable to regular values in a type. They will reduce TypeScript's ability to find bugs in your code.
- Prefer `null` or `undefined` as a special value instead of `0`, `-1`, or `""`.
- Consider using a tagged union rather than `null` or `undefined` if the meaning of those values isn't clear.

## Code Samples

```ts
function splitAround<T>(vals: readonly T[], val: T): [T[], T[]] {
  const index = vals.indexOf(val);
  return [vals.slice(0, index), vals.slice(index+1)];
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwA4BsZQIICc7gAmAPACoB8AFAG4CG6yAXIrgKa2ELoCeipA2gF0ANIjrpmpAJTN+AkXyGDEAbwBQiRBATIoiGGEKsAHogC8Y+sgB0Bo8YDywGvSkBuDS1ZQQuJP3EbZEwIVkoABlE7EylRQOtgmFDKaOMAagBGKUEPAF81IA)

----

```ts
function safeIndexOf<T>(vals: readonly T[], val: T): number | null {
  const index = vals.indexOf(val);
  return index === -1 ? null : index;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwIbAKYEkwBMMAeA8sADwAqAfABQBuqANsgFyIBOGquCDAnouQDaAXQA0ieg1bkAlKzAgAtgCMMbRAB9EChg0QBvAFCJEEBMiiIYeQogC8ExsgB01-MWB1GMgNzH2GFAgbEhutnYRiAC0AIyIAPzaILqIrGEEfgC+hkA)

----

```ts
function splitAround<T>(vals: readonly T[], val: T): [T[], T[]] {
  const index = safeIndexOf(vals, val);
  return [vals.slice(0, index), vals.slice(index+1)];
  //                    ~~~~~              ~~~~~ 'index' is possibly 'null'
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwIbAKYEkwBMMAeA8sADwAqAfABQBuqANsgFyIBOGquCDAnouQDaAXQA0ieg1bkAlKzAgAtgCMMbRAB9EChg0QBvAFCJEEBMiiIYeQogC8ExsgB01-MWB1GMgNzH2GFAgbEhutnYRiAC0AIyIAPzaILqIrGEEfgC+hqCQsAgoAA4MMFAAgmxw4LgUNJIsAVw8-EJijlICcoiCreKtwgb+ZmAWVjYE9ijo2OMkXkzikr7+HEEh3fXOyCUQGNQADOLpMotOWzt76QDUMTLCfiYA9I8mr2-vHwB+398ff4g-X4AcnSQKsyEQhTgyGQMGUfEQQJ0DCBhmyQA)

----

```ts
function splitAround<T>(vals: readonly T[], val: T): [T[], T[]] {
  const index = safeIndexOf(vals, val);
  if (index === null) {
    return [[...vals], []];
  }
  return [vals.slice(0, index), vals.slice(index+1)];  // ok
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwIbAKYEkwBMMAeA8sADwAqAfABQBuqANsgFyIBOGquCDAnouQDaAXQA0ieg1bkAlKzAgAtgCMMbRAB9EChg0QBvAFCJEEBMiiIYeQogC8ExsgB01-MWB1GMgNzH2GFAgbEhutnYRiAC0AIyIAPzaILqIrGEEfgC+hqCQsAgoAA4MMFAAgmxw4LgUNJIsAVw8-EJijlICcoiCreKtwgb+ZmAWVjYE9ijo2OMkXkzikr7+MMCI1On2kToMMoMmJhxBId2Czuf1bSLCfibZh4HBSIL1zsglEBjUAAzi6TKLJxvD5fdIAahiMhuJgA9DDEHAANaGbJAA)

----

```ts
interface Product {
  title: string;
  priceDollars: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABAZwIbAKYEkwBMMAeA8sADwAqAfABQBuqANsgFyIBOGquCDAnouQDaAXQA0ieg1bkAlKzAgAtgCMMbRAB9EChg0QBvAFCJEEBMiiIYeQogC8ExsgB01-MWB1GMgNzH2GFAgbEhutnYRiAC0AIyIAPzaILqIrGEEfgC+htZQasCoEBiIAApscLgg0Ab+sFAMGKwWbNYA5n4mAA4tRQAicLqobCxJKmpZhkA)

----

```ts
interface Product {
  title: string;
  /** Price of the product in dollars, or -1 if price is unknown */
  priceDollars: number;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgApQPYBMCuCzIDeAUMsmMGADYQBcyAzmFKAOYDcpyA9AFS9oWSZBhjkAFigAOmXPmShkWDFSpwoDADQioyALQBGBWJnBhwBshwgA1iAwB3EMl7cuppABEVajfRA4ALYARtCcAL7EQA)

----

```ts
// @strictNullChecks: false
const truck: Product = {
  title: 'Tesla Cybertruck',
  priceDollars: null,  // ok
};
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5&strictNullChecks=false#code/JYOwLgpgTgZghgYwgAgApQPYBMCuCzIDeAUMsmMGADYQBcyAzmFKAOYDcpyA9AFS9oWSZBhjkAFigAOmXPmShkWDFSpwoDADQioyALQBGBWJnBhwBshwgA1iAwB3EMl7cuppABEVajfRA4ALYARtCcAL7E3NzIAAJMQmAAcjiqAMKSCDYM9PBUDBDECBggTORQeDb06Nh4BAC8RFwU1HTIAOQAKhAMashpAJ6hUMyV7ZruQhDequo5yAGq2jwxGDbE4ZxAA)


# Item 37: Limit the Use of Optional Properties

## Things to Remember

- Optional properties can prevent the type checker from finding bugs and can lead to repeated and possibly inconsistent code for filling in default values.
- Think twice before adding an optional property to an interface. Consider whether you could make it required instead.
- Consider creating distinct types for un-normalized input data and normalized data for use in your code.
- Avoid a combinatorial explosion of options.

## Code Samples

```ts
interface FormattedValue {
  value: number;
  units: string;
}
function formatValue(value: FormattedValue) { /* ... */ }
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGIHsoFs5kgEwDU4AbAVxQG8AoZZAN1IoC5kQysAjaAbluTIhgYAM6sRYKKADmfAL7UYghGGDoQyGJhxhi5CAApG+1hmy4CeigEpklZAHoAVMgB075E4fIFQA)

----

```ts
interface Hike {
  miles: number;
  hours: number;
}
function formatHike({miles, hours}: Hike) {
  const distanceDisplay = formatValue({value: miles, units: 'miles'});
  const paceDisplay = formatValue({value: miles / hours, units: 'mph'});
  return `${distanceDisplay} at ${paceDisplay}`;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/JYOwLgpgTgZghgYwgAgGIHsoFs5kgEwDU4AbAVxQG8AoZZAN1IoC5kQysAjaAbluTIhgYAM6sRYKKADmfAL7UYghGGDoQyGJhxhi5CAApG+1hmy4CeigEpklZAHoAVMgB075E4fIFoSLEQUAAlgAGsqfixgEggxNg5uKD46AAt0Mig49i5eagUlEBU1DS1zMBDwg0oomJEAGmQ0jJE5VgqIWxo6BHUJZHxgCThCiAARQYAHEjgAT2QAXk1tXCtDSmMWZBrYhsFhOIBybZEDuWtk5B6QPonA8ZEp2YWlstWqjYhWY8dG9MzdoSiVhHCYpU7nfhQCBgDIaAAGABJKAMhiN7o8ZnJkLhkEjbkh0dNMXD5NQgA)

----

```ts
type UnitSystem = 'metric' | 'imperial';
interface FormattedValue {
  value: number;
  units: string;
  /** default is imperial */
  unitSystem?: UnitSystem;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAYgHtSWZsEwATAGpsArtADeXKFABuKiAC4ocZVgBGEUty3LEwNIYzk4AcytQA9ACpPUORCHKrMBQCGghjBYIbFCe7ppQNkioGNgA-IbwSeiYWNwAvlxAA)

----

```ts
interface AppConfig {
  darkMode: boolean;
  // ... other settings ...
  /** default is imperial */
  unitSystem?: UnitSystem;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAYgHtSWZsEwATAGpsArtADeXKFABuKiAC4ocZVgBGEUty3LEwNIYzk4AcytQA9ACpPUORCHKrMBQCGghjBYIbFCe7ppQNkioGNgA-IbwSeiYWNwAvjx8FkIiUACCYGAAwuJwAgjOUBpacsykANYAsuJ+hqbi4qwQzHBu7u5QAHTTUOLAABYWUGgkwLzOYdOT8V4+fgFBIWEMTFGsMXHWtsk56bDX2dj5XEA)

----

```ts
function formatHike({miles, hours}: Hike, config: AppConfig) {
  const { unitSystem } = config;
  const distanceDisplay = formatValue({
    value: miles, units: 'miles', unitSystem
  });
  const paceDisplay = formatValue({
    value: miles / hours, units: 'mph'  // forgot unitSystem, oops!
  });
  return `${distanceDisplay} at ${paceDisplay}`;
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAYgHtSWZsEwATAGpsArtADeXKFABuKiAC4ocZVgBGEUty3LEwNIYzk4AcytQA9ACpPUORCHKrMBQCGghjBYIbFCe7ppQNkioGNgA-IbwSeiYWNwAvjx8FkIiUACCYGAAwuJwAgjOUBpacsykANYAsuJ+hqbi4qwQzHBu7u5QAHTTUOLAABYWUGgkwLzOYdOT8V4+fgFBIWEMTFGsMXHWtsk56bDX2dj5hfwl0AASCO3q8VgIQ-YjCZzJZ4vNxMpSIDjGYLM8BDYKGtalABJJpMAlKxVAAKXTYgxQCRSGTyLGqACUTQ8Pi2FygBQRcCRCBRaJJwE+3xxaj+AIANFBwZC0HlDFyIIKKLV6s5DBVqjKGlTmlBpXAMNTEihHjg8ng1UrXPF1Zq5KFgCMRAARUJgVjMEAG9kY8kQHnxLT41SGPkQNCC7WAoj-f0EQMPFJYeJ5CluU3BMDCCC2tD2x3O9EyN0erRevS+0NhCbCqERpDBxjzageCbs5xzBKRnKCgZgNAAQhjcfipBIkLgUAABgASNTmjBWlN2h0gfUyKBjpM2meOvJD55AA)

----

```ts
declare let config: AppConfig;
const unitSystem = config.unitSystem ?? 'imperial';
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAYgHtSWZsEwATAGpsArtADeXKFABuKiAC4ocZVgBGEUty3LEwNIYzk4AcytQA9ACpPUORCHKrMBQCGghjBYIbFCe7ppQNkioGNgA-IbwSeiYWNwAvjx8FkIiUACCYGAAwuJwAgjOUBpacsykANYAsuJ+hqbi4qwQzHBu7u5QAHTTUOLAABYWUGgkwLzOYdOT8V4+fgFBIWEMTFGsMXHWtsk56bDX2dj5hfwl0AASCO3q8VgIQ-YjCZzJZ4vNxMpSIDjGYLM8BDYKGtalABJJpMAlKxVAAKXTYgxQCRSGTyLGqACUTQ8Pi2FygBT8FFYbWgQ2CFFq9Wchgq1S5DW4nLgGASDxSOHwwu5k0SKEeOFSqXoERY7G4QA)

----

```ts
const unitSystem = config.unitSystem ?? 'metric';
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAYgHtSWZsEwATAGpsArtADeXKFABuKiAC4ocZVgBGEUty3LEwNIYzk4AcytQA9ACpPUORCHKrMBQCGghjBYIbFCe7ppQNkioGNgA-IbwSeiYWNwAvjx8FkIiUACCYGAAwuJwAgjOUBpacsykANYAsuJ+hqbi4qwQzHBu7u5QAHTTUOLAABYWUGgkwLzOYdOT8V4+fgFBIWEMTFGsMXHWtsk56bDX2dj5hfwl0AASCO3q8VgIQ-YjCZzJZ4vNxMpSIDjGYLM8BDYKGtalABJJpMAlKxVAAKXTYgxQCRSGTyLGqACUTQ8Pi2FygBT8FFYbWgQ2CFFq9Wchgq1S5DW4nLgGASDxSOHwwu5k0SKEeOFSqUIxDIlE4XCAA)

----

```ts
interface InputAppConfig {
  darkMode: boolean;
  // ... other settings ...
  /** default is imperial */
  unitSystem?: UnitSystem;
}
interface AppConfig extends InputAppConfig {
  unitSystem: UnitSystem;  // required
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAknDABXYAEEwYAMIB7OAIQBzKAG8uUKABNmpANYBZJfogAuKACMlS1hGZxuegPTuoAOl9QlwAAWEKRQaCTAvOpoPr66UO4AVIkGEEKSrMBQCDEMTAhsUInu8ZKIKOiYWAD8NvBIqBjY3AC+PHwhQiJQcooqapoQAB6YcPox4lKy8sqqGtql5Y1VdUuVzR5epBAAjpII2-pcbUA)

----

```ts
function normalizeAppConfig(inputConfig: InputAppConfig): AppConfig {
  return {
    ...inputConfig,
    unitSystem: inputConfig.unitSystem ?? 'imperial',
  };
}
```

[💻 playground](https://www.typescriptlang.org/play/?ts=5.4.5#code/C4TwDgpgBAqgdgS2AZRAZ2BAtlAvFAciwmACcEBjAqAH0IS0nIEMAbAgbgCgE5NSAZswrQAknDABXYAEEwYAMIB7OAIQBzKAG8uUKABNmpANYBZJfogAuKACMlS1hGZxuegPTuoAOl9QlwAAWEKRQaCTAvOpoPr66UO4AVIkGEEKSrMBQCDEMTAhsUInu8ZKIKOiYWAD8NvBIqBjY3AC+PHwhQiJQcooqapoQAB6YcPox4lKy8sqqGtql5Y1VdUuVzR5epBAAjpII2-pcbQJlFJEqUHBKpFhsCABeEL2zAwAUvFOvGjaT0i-9DQAShsALmmh0em2wEkpDgCz0el83k+0m+6gANPE9GUGussDZUcB0d5cRUmjhqtV6IwQgV2Fi9C1WlwgA)



# Quotes


# References
- https://www.typescriptlang.org/docs/handbook/
- https://www.typescriptlang.org/play
- https://github.com/danvk/effective-typescript
- https://effectivetypescript.com/
- https://github.com/microsoft/TypeScript/wiki/Performance
- https://google.github.io/styleguide/tsguide.html
