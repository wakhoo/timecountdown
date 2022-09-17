/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig
// module.exports = () => {
//   const rewrites = () => {
//     return [
//       {
//         source: "/main/:path*",
//         destination: "http://localhost:5050/main/:path*",
//       },
//     ];
//   };
//   return {
//     rewrites,
//   };
// };