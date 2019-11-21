![](http://flyer-app.org/images/initial_logo_color.png =250x)

# Application and Dashboard Backend
This application backend is the backbone connection between the flyer organiser dashboard and the flyer app itself. The backend api builds up on a graphql implementation called [graphql-yoga](https://github.com/prisma-labs/graphql-yoga) with [prisma.io](https://prisma.io) as database accessor.

## Tech and Frameworks
This application uses a number of open source projects to work properly:
* [graphql-yoga](https://github.com/prisma-labs/graphql-yoga) - A GraphQL implementation
* [prisma.io](https://prisma.io) - Database access and design tool
* [Docker](https://docker.com) - An application container
* [Jest](https://jestjs.io) - A JS testing tool

## Development
For development purpose please clone the project and open up your own development branch from the main development branch. After testing and deciding to take the changes merge with master branch.

```sh
$ git checkout -b development-[what-you-develop]
$ git checkout master && git merge development-[what-you-develop]
```

### Testing
If you want to test your code - we pre-installed jest. Please use as described in their docs.
For eg.:

```sh
$ jest user.test.js OR npm run test user.test.js
```

## Hotfix Branch
For any hotfix you have please branch and then after testing your fix merge branches.

```sh
$ git checkout -b hotfix-[what-you-fix]
$ git checkout master && git merge hotfix-[what-you-fix]
```

## Feature Branch
If you have a new feature open, on your developer branch, a new feature branch. After deciding to accept the feature merge into master branch.

```sh
$ git checkout -b feature-[give-it-a-name]
$ git checkout master && git merge feature-[give-it-a-name]
```

# Server
Cause this is a nodejs based server, please use the scripts based in 'package.json'. Thank you and start the server with:

```sh
$ node index.js OR npm start
```

# License

This project is licensed under the ISC License
