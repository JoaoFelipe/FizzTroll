require 'fizz_troll'

describe 'FizzTroll' do
  functions = [
    proc {|n| fizz_buzz(n)},
    proc {|n| fizz_intro(n)},
    proc {|n| n.fizz_in},
    proc {|n| fizz_map(n)},
    proc {|n| fizz_select(n)},
  ]

  it 'should say 1 when 1 was given' do
    functions.each{|func| func.call(1).should == 1}
  end
  
  it 'should say 2 when 2 was given' do
    functions.each{|func| func.call(2).should == 2}
  end

  it 'should say fizz when 3 was given' do
    functions.each{|func| func.call(3).should == "fizz"}
  end

  it 'should say buzz when 5 was given' do
    functions.each{|func| func.call(5).should == "buzz"}
  end
  
  it 'should say fizz when 6 was given' do
    functions.each{|func| func.call(6).should == "fizz"}
  end
  
  it 'should say buzz when 10 was given' do
    functions.each{|func| func.call(10).should == "buzz"}
  end
  
  it 'should say fizzbuzz when 15 was given' do
    functions.each{|func| func.call(15).should == "fizzbuzz"}
  end
  
  it 'should say fizzbuzz when 30 was given' do
    functions.each{|func| func.call(30).should == "fizzbuzz"}
  end
end
