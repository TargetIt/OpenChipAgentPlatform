module fifo_sync #(
  parameter int WIDTH = 8,
  parameter int DEPTH = 4
) (
  input  logic             clk,
  input  logic             rst,
  input  logic             push_valid,
  output logic             push_ready,
  input  logic [WIDTH-1:0] push_data,
  output logic             pop_valid,
  input  logic             pop_ready,
  output logic [WIDTH-1:0] pop_data,
  output logic             full,
  output logic             empty
);
  localparam int ADDR_W = $clog2(DEPTH);
  localparam int COUNT_W = $clog2(DEPTH + 1);

  logic [WIDTH-1:0] mem [0:DEPTH-1];
  logic [ADDR_W-1:0] rd_ptr;
  logic [ADDR_W-1:0] wr_ptr;
  logic [COUNT_W-1:0] count;
  localparam logic [COUNT_W-1:0] DEPTH_COUNT = COUNT_W'(DEPTH);

  logic do_push;
  logic do_pop;

  assign full = (count == DEPTH_COUNT);
  assign empty = (count == '0);
  assign push_ready = !full || (pop_valid && pop_ready);
  assign pop_valid = !empty;
  assign pop_data = mem[rd_ptr];
  assign do_push = push_valid && push_ready;
  assign do_pop = pop_valid && pop_ready;

  always_ff @(posedge clk) begin
    if (rst) begin
      rd_ptr <= '0;
      wr_ptr <= '0;
      count <= '0;
    end else begin
      if (do_push) begin
        mem[wr_ptr] <= push_data;
        wr_ptr <= wr_ptr + 1'b1;
      end

      if (do_pop) begin
        rd_ptr <= rd_ptr + 1'b1;
      end

      case ({do_push, do_pop})
        2'b10: count <= count + 1'b1;
        2'b01: count <= count - 1'b1;
        default: count <= count;
      endcase
    end
  end
endmodule
