
//
// C# and Python inspired string templating. Target tokens must be numbered with the index of the 
// replacement string and surrounded by curly brackets; e.g:
//
// 		"{0} {1} {0}".format("foo", "bar");	// "foo bar foo"
//
// The advantage of {n} over '%n' or '$n' is the closing '}' allows for more complex templates
// since the target token can be contiguous with a trailing digit. E.g., it allows "1{0}1".
//
String.prototype.format =
    String.prototype.format ||
    function ()
    {
        // get replacement token array
        var  args = Array.prototype.slice.call(arguments, 0);

        // callback regex engine invokes for each target token '{n}'
        var doReplaceToken = 
            function(targetToken)
            {
                // get n from token with format '{n}' and derive the int value; provides the
                // index n in args[n], i.e. it is index of the string with which to replace
                // the target
                var indexToken = targetToken.substring(1, targetToken.length - 1);

                var index = parseInt(indexToken, 10);

                if(index >= args.length)
                {
                    throw "Token '{0}' contains an index outside the bounds of the argument array.".format(targetToken);
                }

                return args[index];
            }

        return  this.replace(/(\{\d+\})/g, doReplaceToken);
    };
