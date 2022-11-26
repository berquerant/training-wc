const std = @import("std");
const io = std.io;
const mem = std.mem;

pub fn main() !void {
    const stdin = io.getStdIn();
    var bufin = io.bufferedReader(stdin.reader());
    var in = bufin.reader();

    var line: u64 = 0;
    var word: u64 = 0;
    var bytes: u64 = 0;

    const buf_size = 1024 * 4;
    var buf: [buf_size]u8 = undefined;
    while (try in.readUntilDelimiterOrEof(&buf, '\n')) |x| {
        line += 1;
        bytes += @as(u64, x.len) + 1; // + newline

        var it = mem.split(u8, x, " ");
        while (it.next()) |y| {
            if (y.len != 0) word += 1;
        }
    }

    try io.getStdOut().writer().print("{d} {d} {d}\n", .{ line, word, bytes });
}
