function [seq, emit]= markov_sequence(T, s, E, O, f, max_seq)
    % T is M by M matrix containing probability of moving
    % from row state to column state. T(2, 3) = probability
    % of state 2 to state 3 transition.
    % s is a scalar specifying the start state
    % E is M by N matrix containing probability of emitting
    % output N at state M.
    % O is a vector of output values
    % f is a scalar representing a termination state.
    % max_seq is a scalar representing the maximum sequence size.
    seq = [s];
    % initial emission
    emission = min(find(rand < cumsum(E(s,:))));
    emit = [O(emission)];
    while s = f && length(seq) < max_seq
    % transition to new state
    state_vector = T(:,s)';
    p = rand;
    s = min(find(p < cumsum(state_vector)));
    seq = [seq; s];
    % find emission
    emission = min(find(rand < cumsum(E(s,:))));
    emit = [emit; O(emission)];
end
